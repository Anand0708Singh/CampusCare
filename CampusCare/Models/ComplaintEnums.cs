using System.ComponentModel.DataAnnotations;

namespace CampusCare.Models
{
    public enum ComplaintPriority
    {
        [Display(Name = "Low")]
        Low = 1,

        [Display(Name = "Medium")]
        Medium = 2,

        [Display(Name = "High")]
        High = 3,

        [Display(Name = "Urgent / Emergency")]
        Urgent = 4
    }

    public enum ComplaintStatus
    {
        [Display(Name = "Open")]
        Open = 1,

        [Display(Name = "In Progress")]
        InProgress = 2,

        [Display(Name = "Resolved")]
        Resolved = 3,

        [Display(Name = "Closed / Rejected")]
        Closed = 4
    }
}

