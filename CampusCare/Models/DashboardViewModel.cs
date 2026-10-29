namespace CampusCare.Models
{
    public class DashboardViewModel
    {
        public int TotalCount { get; set; }
        public int OpenCount { get; set; }
        public int InProgressCount { get; set; }
        public int ResolvedCount { get; set; }
        public int UrgentCount { get; set; }

        public List<Complaint> Complaints { get; set; } = new();
        public List<Category> Categories { get; set; } = new();

        // Filters
        public string? SearchKeyword { get; set; }
        public int? SelectedCategoryId { get; set; }
        public ComplaintStatus? SelectedStatus { get; set; }
        public ComplaintPriority? SelectedPriority { get; set; }
    }
}

