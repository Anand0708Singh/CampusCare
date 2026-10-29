using System.ComponentModel.DataAnnotations;

namespace CampusCare.Models
{
    public class Category
    {
        public int Id { get; set; }

        [Required(ErrorMessage = "Category name is required.")]
        [StringLength(50, MinimumLength = 2, ErrorMessage = "Category name must be between 2 and 50 characters.")]
        public string Name { get; set; } = string.Empty;

        [Required(ErrorMessage = "Department is required.")]
        [StringLength(80)]
        public string Department { get; set; } = string.Empty;

        [StringLength(50)]
        public string IconClass { get; set; } = "bi-wrench";

        public ICollection<Complaint> Complaints { get; set; } = new List<Complaint>();
    }
}

