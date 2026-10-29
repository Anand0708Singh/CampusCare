import os
import textwrap
from reportlab.lib.pagesizes import A2
from reportlab.lib import colors
from reportlab.pdfgen import canvas

def create_a2_poster(filename="poster/CampusCare - A2 Project Poster.pdf"):
    W, H = A2 # 1190.55 pt x 1683.78 pt (Exact A2: 420mm x 594mm)
    c = canvas.Canvas(filename, pagesize=A2)

    # 1. Dark Backdrop
    c.setFillColor(colors.HexColor("#0A1128"))
    c.rect(0, 0, W, H, fill=1, stroke=0)

    # Outer Sheet Framing
    margin = 16
    pw = W - (2 * margin) # 1158.55 pt
    ph = H - (2 * margin) # 1651.78 pt

    c.setFillColor(colors.HexColor("#F8FAFC"))
    c.setStrokeColor(colors.HexColor("#1E3A8A"))
    c.setLineWidth(5)
    c.roundRect(margin, margin, pw, ph, radius=14, fill=1, stroke=1)

    # 2. Executive Header Banner
    hx = margin + 14
    hy = H - margin - 222
    hw = pw - 28
    hh = 208

    # Dark Navy Header Background
    c.setFillColor(colors.HexColor("#0B192C"))
    c.roundRect(hx, hy, hw, hh, radius=12, fill=1, stroke=0)
    
    # Left Cyan Accent Bar
    c.setFillColor(colors.HexColor("#0284C7"))
    c.roundRect(hx, hy, 12, hh, radius=5, fill=1, stroke=0)

    # 2.1 LOGO 1: UTU Logo (Left Upper Side)
    logo_w, logo_h = 135, 140
    logo1_x = hx + 24
    logo1_y = hy + (hh - logo_h) / 2
    c.setFillColor(colors.white)
    c.roundRect(logo1_x - 8, logo1_y - 8, logo_w + 16, logo_h + 16, radius=10, fill=1, stroke=0)
    
    utu_path = os.path.abspath(r"poster/utu logo.jpg")
    if os.path.exists(utu_path):
        c.drawImage(utu_path, logo1_x, logo1_y, width=logo_w, height=logo_h, preserveAspectRatio=True, mask='auto')

    # 2.2 LOGO 2: AMTICS Logo (Right Upper Side)
    logo2_x = hx + hw - logo_w - 24
    logo2_y = logo1_y
    c.setFillColor(colors.white)
    c.roundRect(logo2_x - 8, logo2_y - 8, logo_w + 16, logo_h + 16, radius=10, fill=1, stroke=0)
    
    amtics_path = os.path.abspath(r"poster/amtics logo.png")
    if os.path.exists(amtics_path):
        c.drawImage(amtics_path, logo2_x, logo2_y, width=logo_w, height=logo_h, preserveAspectRatio=True, mask='auto')

    # 2.3 CENTER HEADER: University, Department, Project Title & Candidate Info
    center_x = W / 2

    # University & Institute Names
    c.setFillColor(colors.HexColor("#38BDF8"))
    c.setFont("Helvetica-Bold", 15)
    c.drawCentredString(center_x, hy + hh - 26, "UKA TARSADIA UNIVERSITY")

    c.setFillColor(colors.HexColor("#BAE6FD"))
    c.setFont("Helvetica-Bold", 12.5)
    c.drawCentredString(center_x, hy + hh - 46, "Asha M. Tarsadia Institute of Computer Science and Technology (AMTICS)")

    # Course
    c.setFillColor(colors.HexColor("#7DD3FC"))
    c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(center_x, hy + hh - 66, "B.Tech Computer Science & Engineering (Cyber Security) • Academic Year 2026-27")

    # Project Title
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 26)
    c.drawCentredString(center_x, hy + hh - 98, "CampusCare: Smart Campus Facility & Complaint Tracker")

    # Subtitle
    c.setFillColor(colors.HexColor("#38BDF8"))
    c.setFont("Helvetica-Bold", 12.5)
    c.drawCentredString(center_x, hy + hh - 120, "Course: Web Technologies with .NET (ASP.NET Core MVC, EF Core & MySQL)")

    # Metadata Ribbon Container (Clean Student & Division Information)
    meta_box_w = 680
    meta_box_h = 42
    meta_box_x = center_x - (meta_box_w / 2)
    meta_box_y = hy + 14

    c.setFillColor(colors.HexColor("#1E293B"))
    c.setStrokeColor(colors.HexColor("#334155"))
    c.setLineWidth(1.5)
    c.roundRect(meta_box_x, meta_box_y, meta_box_w, meta_box_h, radius=8, fill=1, stroke=1)

    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(center_x, meta_box_y + 24, "Student Name: Singh Anand Rajkishor    |    Enrollment No: 202403103510368")

    c.setFillColor(colors.HexColor("#4ADE80"))
    c.setFont("Helvetica-Bold", 10.5)
    c.drawCentredString(center_x, meta_box_y + 8, "Department: B.Tech CSE (Cyber Security)    |    Division: 5F")

    # 3. Three-Column Layout Setup
    # The columns extend from bottom margin up to hy
    bot_y = margin + 14
    col_h = hy - bot_y - 12 # 1651.78 - 30 - 222 = ~1399 pt of pure vertical canvas
    col_gap = 16
    col_w = (pw - 28 - (2 * col_gap)) / 3 # ~365 pt width each

    col1_x = hx
    col2_x = col1_x + col_w + col_gap
    col3_x = col2_x + col_w + col_gap

    # Reusable Card Drawing Function with Top-Down Placement
    def draw_topdown_card(x, top_y, w, h, title, icon_num):
        # top_y is the top edge of the card
        # bottom is top_y - h
        bottom_y = top_y - h
        c.setFillColor(colors.white)
        c.setStrokeColor(colors.HexColor("#CBD5E1"))
        c.setLineWidth(1.8)
        c.roundRect(x, bottom_y, w, h, radius=9, fill=1, stroke=1)

        # Header bar at top of card
        hdr_h = 38
        c.setFillColor(colors.HexColor("#F1F5F9"))
        c.roundRect(x, top_y - hdr_h, w, hdr_h, radius=9, fill=1, stroke=0)
        c.rect(x, top_y - hdr_h, w, 12, fill=1, stroke=0) # flatten lower corners

        # Icon pill
        c.setFillColor(colors.HexColor("#1E3A8A"))
        c.circle(x + 22, top_y - 19, 12, fill=1, stroke=0)
        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold", 11)
        c.drawCentredString(x + 22, top_y - 23, str(icon_num))

        # Card Title
        c.setFillColor(colors.HexColor("#0F172A"))
        c.setFont("Helvetica-Bold", 12.5)
        c.drawString(x + 42, top_y - 24, title)

        return bottom_y

    # Helper function to render text that wraps safely inside cards
    def wrap_text(text, max_chars):
        return textwrap.wrap(text, width=max_chars)

    # ==================== COLUMN 1 ====================
    # Cards: 1. Problem Statement, 2. Objectives, 3. Tech Stack, 4. Architecture
    c1_gap = 14
    c1_top = hy - 12
    # Total available height = col_h. 3 gaps of 14 = 42pt. Total card heights = col_h - 42.
    c1_h1 = 260
    c1_h2 = 320
    c1_h3 = 330
    c1_h4 = col_h - (c1_h1 + c1_h2 + c1_h3 + (3 * c1_gap))

    # --- Card 1: Problem Statement ---
    card1_bot = draw_topdown_card(col1_x, c1_top, col_w, c1_h1, "1. Problem Statement & Motivation", "1")
    p1_desc = "In collegiate institutions, physical equipment failures (lab projectors, split ACs, electrical wiring, LAN connectivity, plumbing breakdowns) are recorded manually in paper logbooks or informal chat channels. This creates acute operational bottlenecks across campus facilities:"
    cur_y = c1_top - 54
    c.setFont("Helvetica", 9.8)
    c.setFillColor(colors.HexColor("#334155"))
    for l in wrap_text(p1_desc, 46):
        c.drawString(col1_x + 16, cur_y, l)
        cur_y -= 15

    cur_y -= 6
    bullet_items_1 = [
        ("• 70%+ Resolution Delays: Zero centralized dispatch or SLA tracking.", 44),
        ("• Zero Transparency: Students and faculty cannot track repair status.", 44),
        ("• Fragmented Records: Lost tickets, duplicate entries, no audit trail.", 44)
    ]
    c.setFont("Helvetica-Bold", 9.8)
    c.setFillColor(colors.HexColor("#DC2626"))
    for b_text, max_c in bullet_items_1:
        for bl in wrap_text(b_text, max_c):
            c.drawString(col1_x + 20, cur_y, bl)
            cur_y -= 15
        cur_y -= 3

    # --- Card 2: Objectives ---
    c1_top2 = card1_bot - c1_gap
    card2_bot = draw_topdown_card(col1_x, c1_top2, col_w, c1_h2, "2. Project Objectives", "2")
    objs = [
        ("Centralized Online Portal:", "Lodge verified tickets with location & category in < 60s."),
        ("Automated Lifecycle:", "Manage progression: Open -> In Progress -> Resolved -> Closed."),
        ("Strict Data Integrity:", "Server-side DataAnnotations + Client-side jQuery validation."),
        ("EF Core Code-First ORM:", "Relational MySQL mapping with automatic pre-seeding."),
        ("Operational Analytics:", "Live dashboard displaying resolution SLA rates and breakdown.")
    ]
    cur_y = c1_top2 - 56
    for title, desc in objs:
        c.setFillColor(colors.HexColor("#1E3A8A"))
        c.setFont("Helvetica-Bold", 10.5)
        c.drawString(col1_x + 16, cur_y, "• " + title)
        cur_y -= 15
        c.setFillColor(colors.HexColor("#475569"))
        c.setFont("Helvetica", 9.5)
        for dl in wrap_text(desc, 44):
            c.drawString(col1_x + 28, cur_y, dl)
            cur_y -= 14
        cur_y -= 5

    # --- Card 3: Technology Stack ---
    c1_top3 = card2_bot - c1_gap
    card3_bot = draw_topdown_card(col1_x, c1_top3, col_w, c1_h3, "3. Production Technology Stack", "3")
    techs = [
        ("ASP.NET Core", "FRAMEWORK", "C# Controller & DI Pipeline"),
        ("EF Core", "ORM", "DbContext & Migrations"),
        ("MySQL 8.0", "DATABASE", "ACID Relational Storage"),
        ("Razor Views", "UI ENGINE", "Tag Helpers & Binding"),
        ("Bootstrap 5", "DESIGN", "12-Col Responsive Grid"),
        ("jQuery Unobtrusive", "VALIDATION", "Client Validation Engine")
    ]
    tw = (col_w - 38) / 2
    th = 74
    for idx, (tname, trole, tdesc) in enumerate(techs):
        col_offset = (idx % 2) * (tw + 10)
        row_offset = (idx // 2) * (th + 12)
        tx = col1_x + 14 + col_offset
        ty = c1_top3 - 52 - row_offset - th
        
        c.setFillColor(colors.HexColor("#F8FAFC"))
        c.setStrokeColor(colors.HexColor("#CBD5E1"))
        c.setLineWidth(1.5)
        c.roundRect(tx, ty, tw, th, radius=6, fill=1, stroke=1)
        
        c.setFillColor(colors.HexColor("#1E3A8A"))
        c.setFont("Helvetica-Bold", 10.5)
        c.drawString(tx + 8, ty + 50, tname)
        
        c.setFillColor(colors.HexColor("#0284C7"))
        c.setFont("Helvetica-Bold", 8.5)
        c.drawString(tx + 8, ty + 32, trole)
        
        c.setFillColor(colors.HexColor("#64748B"))
        c.setFont("Helvetica", 7.8)
        c.drawString(tx + 8, ty + 14, tdesc)

    # --- Card 4: Architecture & Pipeline ---
    c1_top4 = card3_bot - c1_gap
    card4_bot = draw_topdown_card(col1_x, c1_top4, col_w, c1_h4, "Architecture & Request Pipeline", "4")
    arch_steps = [
        ("1. Browser Client (HTTP Request)", "User submits ticket form with CSRF token via Bootstrap UI.", "#0284C7"),
        ("2. Routing & Anti-Forgery Filter", "Route matching {controller}/{action} + validates CSRF token.", "#D97706"),
        ("3. Controller & Model Binding", "ComplaintsController validates input via ModelState.IsValid.", "#7C3AED"),
        ("4. EF Core & MySQL Execution", "ApplicationDbContext executes parameterized LINQ against MySQL.", "#059669"),
        ("5. State Management & Response", "TempData[\"SuccessMessage\"] passed to Razor with PRG redirect.", "#0284C7")
    ]
    step_gap = (c1_h4 - 56) / len(arch_steps)
    for idx, (title, desc, colr) in enumerate(arch_steps):
        s_top = c1_top4 - 50 - (idx * step_gap)
        box_h = step_gap - 10
        s_bot = s_top - box_h
        
        # Step Container Box
        c.setFillColor(colors.HexColor("#FFFFFF"))
        c.setStrokeColor(colors.HexColor("#CBD5E1"))
        c.setLineWidth(1.4)
        c.roundRect(col1_x + 14, s_bot, col_w - 28, box_h, radius=6, fill=1, stroke=1)
        
        # Left Colored Accent Bar
        c.setFillColor(colors.HexColor(colr))
        c.roundRect(col1_x + 14, s_bot, 6, box_h, radius=2, fill=1, stroke=0)
        
        # Step Title
        c.setFillColor(colors.HexColor("#0F172A"))
        c.setFont("Helvetica-Bold", 10.5)
        c.drawString(col1_x + 28, s_top - 18, title)
        
        # Step Description (strictly wrapped with 42 chars to stay within margins)
        c.setFillColor(colors.HexColor("#475569"))
        c.setFont("Helvetica", 9)
        cur_desc_y = s_top - 34
        for dl in wrap_text(desc, 42):
            c.drawString(col1_x + 28, cur_desc_y, dl)
            cur_desc_y -= 13

    # ==================== COLUMN 2 (THE 7 CORE CONCEPTS) ====================
    # Outer card holds all 7 concepts cleanly
    col2_top = hy - 12
    draw_topdown_card(col2_x, col2_top, col_w, col_h, "The 7 Core .NET Concepts", "★")

    concepts = [
        ("1. MVC Architectural Pattern", "Separation",
         ["• Model: Complaint.cs & Category.cs define entities.",
          "• View: Razor views (.cshtml) render UI via Tag Helpers.",
          "• Controller: Handles DI, actions, & response pipeline."],
         "public class ComplaintsController : Controller {\n    private readonly ApplicationDbContext _context;\n}"),

        ("2. EF Core Code-First with MySQL", "ORM",
         ["• Configured via Pomelo.EntityFrameworkCore.MySql.",
          "• Auto-seeds 5 Campus Categories & sample tickets."],
         "builder.Services.AddDbContext<ApplicationDbContext>(opt =>\n    opt.UseMySql(connStr, ServerVersion.AutoDetect(connStr)));"),

        ("3. Complete CRUD Operations", "Lifecycle",
         ["• Create: Form POST saves new ticket with urgency.",
          "• Read: Filtered dashboard lists tickets with status.",
          "• Update: Edit action updates technician & remarks.",
          "• Delete: Confirmation modal safely removes ticket."],
         "public async Task<IActionResult> Create(Complaint model) {\n    _context.Add(model); await _context.SaveChangesAsync();\n}"),

        ("4. Form Handling & Anti-Forgery", "CSRF Guard",
         ["• Strongly-typed bindings: asp-for, asp-items, validation-for.",
          "• Protected with [ValidateAntiForgeryToken] against CSRF."],
         "<form asp-action=\"Create\" method=\"post\">\n  @Html.AntiForgeryToken()\n  <input asp-for=\"Title\" class=\"form-control\" />\n</form>"),

        ("5. Model Validation (Server & Client)", "Integrity",
         ["• Server-side: [Required], [StringLength(100)], [EmailAddress].",
          "• Controller check: if (!ModelState.IsValid) return View(model);",
          "• Client-side: Real-time jQuery Unobtrusive validation."],
         "[Required(ErrorMessage = \"Title is required\")]\n[StringLength(100)] public string Title { get; set; }"),

        ("6. State Management (PRG Pattern)", "TempData",
         ["• Post-Redirect-Get pattern with TempData[\"SuccessMessage\"].",
          "• Shows dismissible green toast alert after redirect."],
         "TempData[\"SuccessMessage\"] = $\"Grievance #{model.Id} registered!\";\nreturn RedirectToAction(nameof(Index));"),

        ("7. Responsive UI Design", "Bootstrap 5",
         ["• Mobile-first 12-column grid collapses cleanly on phones.",
          "• Features 4 KPI summary cards, filter bars, & status badges."],
         "<div class=\"card border-0 shadow-sm rounded-4 h-100 p-3\">...</div>")
    ]

    # Available vertical height inside col2 = col_h - 48 (card header) - 16 (bottom padding)
    c2_inner_h = col_h - 64
    concept_h = c2_inner_h / len(concepts) # Height per concept block (~190.5 pt)
    for idx, (ctitle, ctag, cbullet_list, ccode) in enumerate(concepts):
        # Calculate strict top and bottom for this concept block
        block_top = col2_top - 46 - (idx * concept_h)
        block_bot = block_top - (concept_h - 8)
        block_w = col_w - 28
        
        # Outer concept container box
        c.setFillColor(colors.HexColor("#F8FAFC"))
        c.setStrokeColor(colors.HexColor("#BFDBFE"))
        c.setLineWidth(1.4)
        c.roundRect(col2_x + 14, block_bot, block_w, concept_h - 8, radius=7, fill=1, stroke=1)

        # Left Blue Accent
        c.setFillColor(colors.HexColor("#0284C7"))
        c.roundRect(col2_x + 14, block_bot, 5, concept_h - 8, radius=2, fill=1, stroke=0)

        # Header Title
        c.setFillColor(colors.HexColor("#0369A1"))
        c.setFont("Helvetica-Bold", 10.8)
        c.drawString(col2_x + 26, block_top - 18, ctitle)

        # Pill Tag
        c.setFillColor(colors.HexColor("#E0F2FE"))
        tw_tag = c.stringWidth(ctag, "Helvetica-Bold", 8.2) + 14
        c.roundRect(col2_x + col_w - 20 - tw_tag, block_top - 24, tw_tag, 16, radius=4, fill=1, stroke=0)
        c.setFillColor(colors.HexColor("#0369A1"))
        c.setFont("Helvetica-Bold", 8.2)
        c.drawString(col2_x + col_w - 13 - tw_tag, block_top - 20, ctag)

        # Bullet descriptions
        cur_desc_y = block_top - 35
        c.setFillColor(colors.HexColor("#334155"))
        c.setFont("Helvetica", 8.6)
        for bl in cbullet_list:
            for b_line in wrap_text(bl, 46):
                c.drawString(col2_x + 26, cur_desc_y, b_line)
                cur_desc_y -= 12.2

        # Code snippet box dynamically sized based on line count
        code_lines = ccode.split("\n")
        n_lines = len(code_lines)
        code_box_h = 10 + (n_lines * 12)
        code_box_bot = block_bot + 8
        code_box_w = block_w - 24
        
        c.setFillColor(colors.HexColor("#0F172A"))
        c.roundRect(col2_x + 26, code_box_bot, code_box_w, code_box_h, radius=5, fill=1, stroke=0)
        
        c.setFillColor(colors.HexColor("#38BDF8"))
        c.setFont("Courier-Bold", 7.6)
        code_text_y = code_box_bot + code_box_h - 11
        for cl in code_lines:
            c.drawString(col2_x + 34, code_text_y, cl)
            code_text_y -= 12

    # ==================== COLUMN 3 ====================
    # Cards: 6. Modules, 7. UI Walkthrough, 8. Test Matrix, 9. Conclusion
    c3_gap = 14
    c3_top = hy - 12
    c3_h1 = 300
    c3_h2 = 440
    c3_h3 = 330
    c3_h4 = col_h - (c3_h1 + c3_h2 + c3_h3 + (3 * c3_gap))

    # --- Card 6: Implemented Modules ---
    card6_bot = draw_topdown_card(col3_x, c3_top, col_w, c3_h1, "6. Implemented Application Modules", "6")
    mods = [
        ("Student Issue Desk (Create)", "Lodge grievances with Category, Urgency level, Location, and Email."),
        ("Admin Control Center (Index & Edit)", "Filter by department, assign technician, update status, and add remarks."),
        ("SLA & Resolution Analytics", "High-level summary displaying overall resolution rate & category breakdown."),
        ("Safe Removal & Deletion (Delete)", "Two-step confirmation modal preventing accidental ticket elimination.")
    ]
    cur_y = c3_top - 58
    for mname, mdetail in mods:
        c.setFillColor(colors.HexColor("#1E3A8A"))
        c.setFont("Helvetica-Bold", 10.5)
        c.drawString(col3_x + 16, cur_y, "• " + mname)
        cur_y -= 16
        c.setFillColor(colors.HexColor("#475569"))
        c.setFont("Helvetica", 9.2)
        for dl in wrap_text(mdetail, 44):
            c.drawString(col3_x + 28, cur_y, dl)
            cur_y -= 14
        cur_y -= 6

    # --- Card 7: Live UI Walkthrough ---
    c3_top2 = card6_bot - c3_gap
    card7_bot = draw_topdown_card(col3_x, c3_top2, col_w, c3_h2, "7. Live Application UI Walkthrough", "7")
    
    # Outer browser mock window
    bx = col3_x + 14
    bw = col_w - 28
    bh = c3_h2 - 58
    by = c3_top2 - 48 - bh
    
    c.setFillColor(colors.HexColor("#1E293B"))
    c.roundRect(bx, by, bw, bh, radius=8, fill=1, stroke=0)
    
    # Browser Top Bar
    c.setFillColor(colors.HexColor("#0F172A"))
    c.roundRect(bx, by + bh - 24, bw, 24, radius=8, fill=1, stroke=0)
    c.rect(bx, by + bh - 24, bw, 10, fill=1, stroke=0)
    c.setFillColor(colors.HexColor("#EF4444")); c.circle(bx + 14, by + bh - 12, 4.5, fill=1, stroke=0)
    c.setFillColor(colors.HexColor("#F59E0B")); c.circle(bx + 26, by + bh - 12, 4.5, fill=1, stroke=0)
    c.setFillColor(colors.HexColor("#10B981")); c.circle(bx + 38, by + bh - 12, 4.5, fill=1, stroke=0)
    c.setFillColor(colors.HexColor("#94A3B8")); c.setFont("Helvetica", 8.8)
    c.drawString(bx + 52, by + bh - 15, "http://localhost:5000/Complaints (Live Running Application)")

    # Browser Content Body
    cx_in = bx + 8
    cy_in = by + 8
    cw_in = bw - 16
    ch_in = bh - 36
    c.setFillColor(colors.white)
    c.roundRect(cx_in, cy_in, cw_in, ch_in, radius=6, fill=1, stroke=0)

    # 3 Real KPI Stat Cards
    card_w = (cw_in - 18) / 3
    card_h = 60
    stat_data = [("02", "Open Tickets", "#EF4444"), ("01", "In Progress", "#F59E0B"), ("02", "Resolved", "#10B981")]
    for s_i, (num, lbl, clr) in enumerate(stat_data):
        sc_x = cx_in + 4 + s_i * (card_w + 5)
        sc_y = cy_in + ch_in - card_h - 10
        c.setFillColor(colors.HexColor(clr))
        c.roundRect(sc_x, sc_y, card_w, card_h, radius=5, fill=1, stroke=0)
        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold", 18)
        c.drawCentredString(sc_x + card_w/2, sc_y + 26, num)
        c.setFont("Helvetica-Bold", 8.8)
        c.drawCentredString(sc_x + card_w/2, sc_y + 10, lbl.upper())

    # Mini Table with Actual Seeded Records
    tbl_y = cy_in + ch_in - card_h - 28
    c.setFillColor(colors.HexColor("#F1F5F9"))
    c.rect(cx_in + 4, tbl_y - 20, cw_in - 8, 22, fill=1, stroke=0)
    c.setFillColor(colors.HexColor("#475569"))
    c.setFont("Helvetica-Bold", 9)
    c.drawString(cx_in + 10, tbl_y - 14, "ID")
    c.drawString(cx_in + 36, tbl_y - 14, "Grievance Title")
    c.drawString(cx_in + 152, tbl_y - 14, "Location")
    c.drawString(cx_in + 218, tbl_y - 14, "Priority")
    c.drawString(cx_in + 270, tbl_y - 14, "Status")

    actual_rows = [
        ("#1", "Projector HDMI Port Damaged", "Seminar 204", "High", "In Progress", "#FEF3C7", "#B45309"),
        ("#2", "Split AC Leaking Water", "Lab 305", "Urgent", "Open", "#FEE2E2", "#DC2626"),
        ("#3", "Tube Lights Flickering", "Library 1F", "Low", "Resolved", "#DCFCE7", "#15803D"),
        ("#4", "Restroom Tap Broken", "Hostel 3", "High", "Open", "#FEE2E2", "#DC2626")
    ]
    r_y = tbl_y - 44
    for rid, rtitle, rroom, rprio, rstat, bbg, bfg in actual_rows:
        c.setFillColor(colors.HexColor("#1E293B"))
        c.setFont("Helvetica-Bold", 9)
        c.drawString(cx_in + 10, r_y, rid)
        c.setFont("Helvetica", 8.8)
        c.drawString(cx_in + 36, r_y, rtitle[:20] + "...")
        c.drawString(cx_in + 152, r_y, rroom)
        c.drawString(cx_in + 218, r_y, rprio)

        # Status Badge Pill
        c.setFillColor(colors.HexColor(bbg))
        c.roundRect(cx_in + 266, r_y - 3, 50, 14, radius=3, fill=1, stroke=0)
        c.setFillColor(colors.HexColor(bfg))
        c.setFont("Helvetica-Bold", 7.6)
        c.drawCentredString(cx_in + 291, r_y + 1, rstat)

        c.setStrokeColor(colors.HexColor("#F1F5F9"))
        c.setLineWidth(1)
        c.line(cx_in + 4, r_y - 8, cx_in + cw_in - 4, r_y - 8)
        r_y -= 30

    # --- Card 8: Testing Matrix ---
    c3_top3 = card7_bot - c3_gap
    card8_bot = draw_topdown_card(col3_x, c3_top3, col_w, c3_h3, "8. Verification & Test Case Matrix", "8")
    tests = [
        ("TC-01: Empty Form Submission", "Triggers DataAnnotations; blocks commit", "PASS"),
        ("TC-02: Valid Ticket Creation", "Persists to MySQL; triggers TempData toast", "PASS"),
        ("TC-03: Lifecycle Progression", "Open -> In Progress -> Resolved advance", "PASS"),
        ("TC-04: Anti-CSRF Guard", "Blocks unauthorized external POST requests", "PASS"),
        ("TC-05: Mobile Layout Rendering", "Bootstrap 12-col grid collapses gracefully", "PASS"),
        ("TC-06: Pre-Seeded Startup", "DbInitializer seeds categories & tickets", "PASS")
    ]
    t_gap = (c3_h3 - 56) / len(tests)
    for idx, (t_id, t_expect, t_res) in enumerate(tests):
        cur_ty = c3_top3 - 54 - (idx * t_gap)
        c.setFillColor(colors.HexColor("#0F172A"))
        c.setFont("Helvetica-Bold", 10.2)
        c.drawString(col3_x + 16, cur_ty, t_id)
        
        c.setFillColor(colors.HexColor("#475569"))
        c.setFont("Helvetica", 9.2)
        c.drawString(col3_x + 28, cur_ty - 14, t_expect)

        # PASS Badge
        c.setFillColor(colors.HexColor("#10B981"))
        c.roundRect(col3_x + col_w - 62, cur_ty - 8, 44, 18, radius=4, fill=1, stroke=0)
        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold", 9)
        c.drawCentredString(col3_x + col_w - 40, cur_ty - 4, t_res)

    # --- Card 9: Conclusion & Future Scope ---
    c3_top4 = card8_bot - c3_gap
    card9_bot = draw_topdown_card(col3_x, c3_top4, col_w, c3_h4, "9. Conclusion & Future Enhancements", "9")
    conc_text = "CampusCare fully satisfies the academic evaluation criteria: clean MVC separation, resilient EF Core database connectivity, robust server & client validation, TempData state management, and responsive presentation."
    cur_y = c3_top4 - 56
    c.setFont("Helvetica", 9.8)
    c.setFillColor(colors.HexColor("#334155"))
    for l in wrap_text(conc_text, 46):
        c.drawString(col3_x + 16, cur_y, l)
        cur_y -= 15

    cur_y -= 8
    c.setFont("Helvetica-Bold", 10.5)
    c.setFillColor(colors.HexColor("#1E3A8A"))
    c.drawString(col3_x + 16, cur_y, "Planned Future Scope:")
    cur_y -= 18

    f_items = [
        "• Institutional Single Sign-On (SSO) via ASP.NET Core Identity.",
        "• Automated Email/SMS alerts on ticket status changes via SendGrid.",
        "• Automated maintenance dispatch via smart campus IoT sensors."
    ]
    c.setFont("Helvetica", 9.2)
    c.setFillColor(colors.HexColor("#475569"))
    for fi in f_items:
        for fl in wrap_text(fi, 44):
            c.drawString(col3_x + 24, cur_y, fl)
            cur_y -= 14
        cur_y -= 4

    c.save()
    print("A2 Poster generated successfully at:", os.path.abspath(filename))

if __name__ == "__main__":
    create_a2_poster()
    create_a2_poster("poster/CampusCare_A2_Poster.pdf")
