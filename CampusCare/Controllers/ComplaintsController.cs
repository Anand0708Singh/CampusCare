using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Rendering;
using Microsoft.EntityFrameworkCore;
using CampusCare.Data;
using CampusCare.Models;

namespace CampusCare.Controllers
{
    public class ComplaintsController : Controller
    {
        private readonly ApplicationDbContext _context;

        public ComplaintsController(ApplicationDbContext context)
        {
            _context = context;
        }

        // ==========================================
        // 1. READ: Dashboard & Complaint List
        // ==========================================
        public async Task<IActionResult> Index(string? searchKeyword, int? categoryId, ComplaintStatus? status, ComplaintPriority? priority)
        {
            // Set session state indicator for user tracking
            HttpContext.Session.SetString("LastVisitedModule", "ComplaintsDashboard");

            var query = _context.Complaints
                .Include(c => c.Category)
                .AsQueryable();

            if (!string.IsNullOrWhiteSpace(searchKeyword))
            {
                query = query.Where(c => c.Title.Contains(searchKeyword) 
                                      || c.Location.Contains(searchKeyword) 
                                      || c.ReporterName.Contains(searchKeyword));
            }

            if (categoryId.HasValue && categoryId.Value > 0)
            {
                query = query.Where(c => c.CategoryId == categoryId.Value);
            }

            if (status.HasValue)
            {
                query = query.Where(c => c.Status == status.Value);
            }

            if (priority.HasValue)
            {
                query = query.Where(c => c.Priority == priority.Value);
            }

            var allComplaints = await _context.Complaints.ToListAsync();

            var viewModel = new DashboardViewModel
            {
                TotalCount = allComplaints.Count,
                OpenCount = allComplaints.Count(c => c.Status == ComplaintStatus.Open),
                InProgressCount = allComplaints.Count(c => c.Status == ComplaintStatus.InProgress),
                ResolvedCount = allComplaints.Count(c => c.Status == ComplaintStatus.Resolved),
                UrgentCount = allComplaints.Count(c => c.Priority == ComplaintPriority.Urgent && c.Status != ComplaintStatus.Resolved && c.Status != ComplaintStatus.Closed),
                Complaints = await query.OrderByDescending(c => c.CreatedAt).ToListAsync(),
                Categories = await _context.Categories.ToListAsync(),
                SearchKeyword = searchKeyword,
                SelectedCategoryId = categoryId,
                SelectedStatus = status,
                SelectedPriority = priority
            };

            return View(viewModel);
        }

        // ==========================================
        // 2. READ: Single Complaint Details
        // ==========================================
        public async Task<IActionResult> Details(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var complaint = await _context.Complaints
                .Include(c => c.Category)
                .FirstOrDefaultAsync(m => m.Id == id);

            if (complaint == null)
            {
                return NotFound();
            }

            return View(complaint);
        }

        // ==========================================
        // 3. CREATE: Lodge New Complaint
        // ==========================================
        public async Task<IActionResult> Create()
        {
            ViewBag.Categories = new SelectList(await _context.Categories.ToListAsync(), "Id", "Name");
            return View();
        }

        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("Title,Description,Location,CategoryId,Priority,ReporterName,ReporterEmail,ReporterPhone")] Complaint complaint)
        {
            if (ModelState.IsValid)
            {
                complaint.CreatedAt = DateTime.Now;
                complaint.Status = ComplaintStatus.Open;

                _context.Add(complaint);
                await _context.SaveChangesAsync();

                // STATE MANAGEMENT: TempData flash alert for Post-Redirect-Get pattern
                TempData["SuccessMessage"] = $"Grievance #{complaint.Id} '{complaint.Title}' has been registered successfully! Maintenance team has been alerted.";
                return RedirectToAction(nameof(Index));
            }

            // If invalid, repopulate category dropdown and show validation errors
            ViewBag.Categories = new SelectList(await _context.Categories.ToListAsync(), "Id", "Name", complaint.CategoryId);
            TempData["ErrorMessage"] = "Please correct the highlighted validation errors and submit again.";
            return View(complaint);
        }

        // ==========================================
        // 4. UPDATE: Edit Status & Administrative Action
        // ==========================================
        public async Task<IActionResult> Edit(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var complaint = await _context.Complaints.FindAsync(id);
            if (complaint == null)
            {
                return NotFound();
            }

            ViewBag.Categories = new SelectList(await _context.Categories.ToListAsync(), "Id", "Name", complaint.CategoryId);
            return View(complaint);
        }

        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Edit(int id, [Bind("Id,Title,Description,Location,CategoryId,Priority,Status,ReporterName,ReporterEmail,ReporterPhone,CreatedAt,AdminRemarks,AssignedTechnician")] Complaint complaint)
        {
            if (id != complaint.Id)
            {
                return NotFound();
            }

            if (ModelState.IsValid)
            {
                try
                {
                    complaint.UpdatedAt = DateTime.Now;
                    _context.Update(complaint);
                    await _context.SaveChangesAsync();

                    TempData["SuccessMessage"] = $"Complaint #{complaint.Id} was successfully updated to status: {complaint.Status}!";
                }
                catch (DbUpdateConcurrencyException)
                {
                    if (!ComplaintExists(complaint.Id))
                    {
                        return NotFound();
                    }
                    else
                    {
                        throw;
                    }
                }
                return RedirectToAction(nameof(Index));
            }

            ViewBag.Categories = new SelectList(await _context.Categories.ToListAsync(), "Id", "Name", complaint.CategoryId);
            TempData["ErrorMessage"] = "Validation failed during update. Please inspect all fields.";
            return View(complaint);
        }

        // Quick Status Advance (e.g., from Dashboard)
        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> QuickStatusUpdate(int id, ComplaintStatus newStatus)
        {
            var complaint = await _context.Complaints.FindAsync(id);
            if (complaint != null)
            {
                complaint.Status = newStatus;
                complaint.UpdatedAt = DateTime.Now;
                await _context.SaveChangesAsync();
                TempData["SuccessMessage"] = $"Ticket #{id} transitioned to '{newStatus}' successfully.";
            }
            return RedirectToAction(nameof(Index));
        }

        // ==========================================
        // 5. DELETE: Remove Ticket (With confirmation)
        // ==========================================
        public async Task<IActionResult> Delete(int? id)
        {
            if (id == null)
            {
                return NotFound();
            }

            var complaint = await _context.Complaints
                .Include(c => c.Category)
                .FirstOrDefaultAsync(m => m.Id == id);

            if (complaint == null)
            {
                return NotFound();
            }

            return View(complaint);
        }

        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> DeleteConfirmed(int id)
        {
            var complaint = await _context.Complaints.FindAsync(id);
            if (complaint != null)
            {
                _context.Complaints.Remove(complaint);
                await _context.SaveChangesAsync();
                TempData["WarningMessage"] = $"Grievance record #{id} was permanently removed.";
            }

            return RedirectToAction(nameof(Index));
        }

        // ==========================================
        // 6. ANALYTICS & FACILITY SUMMARY
        // ==========================================
        public async Task<IActionResult> Analytics()
        {
            var complaints = await _context.Complaints.Include(c => c.Category).ToListAsync();
            return View(complaints);
        }

        private bool ComplaintExists(int id)
        {
            return _context.Complaints.Any(e => e.Id == id);
        }
    }
}

