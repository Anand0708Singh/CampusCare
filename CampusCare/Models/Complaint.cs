using System.ComponentModel.DataAnnotations;

namespace CampusCare.Models
{
    public class Complaint
    {
        public int Id { get; set; }

        [Required(ErrorMessage = "Please provide an issue title.")]
        [StringLength(100, MinimumLength = 5, ErrorMessage = "Title must be between 5 and 100 characters.")]
        [Display(Name = "Issue Title")]
        public string Title { get; set; } = string.Empty;

        [Required(ErrorMessage = "Please provide a detailed description of the problem.")]
        [StringLength(1000, MinimumLength = 10, ErrorMessage = "Description must be between 10 and 1000 characters.")]
        [Display(Name = "Detailed Description")]
        public string Description { get; set; } = string.Empty;

        [Required(ErrorMessage = "Location or Room number is required.")]
        [StringLength(80, ErrorMessage = "Location cannot exceed 80 characters.")]
        [Display(Name = "Location / Room No.")]
        public string Location { get; set; } = string.Empty;

        [Required(ErrorMessage = "Please select an issue category.")]
        [Display(Name = "Category")]
        public int CategoryId { get; set; }

        public Category? Category { get; set; }

        [Required]
        [Display(Name = "Priority Level")]
        public ComplaintPriority Priority { get; set; } = ComplaintPriority.Medium;

        [Required]
        [Display(Name = "Current Status")]
        public ComplaintStatus Status { get; set; } = ComplaintStatus.Open;

        [Required(ErrorMessage = "Your name is required.")]
        [StringLength(60, ErrorMessage = "Name cannot exceed 60 characters.")]
        [Display(Name = "Reported By (Name)")]
        public string ReporterName { get; set; } = string.Empty;

        [Required(ErrorMessage = "Contact email is required.")]
        [EmailAddress(ErrorMessage = "Please enter a valid college email address.")]
        [StringLength(100)]
        [Display(Name = "Contact Email")]
        public string ReporterEmail { get; set; } = string.Empty;

        [Phone(ErrorMessage = "Please enter a valid phone number.")]
        [StringLength(15)]
        [Display(Name = "Phone Number (Optional)")]
        public string? ReporterPhone { get; set; }

        [Display(Name = "Date Reported")]
        public DateTime CreatedAt { get; set; } = DateTime.Now;

        [Display(Name = "Last Updated")]
        public DateTime? UpdatedAt { get; set; }

        [Display(Name = "Admin / Technician Remarks")]
        [StringLength(500)]
        public string? AdminRemarks { get; set; }

        [Display(Name = "Assigned Technician")]
        [StringLength(80)]
        public string? AssignedTechnician { get; set; }
    }
}

