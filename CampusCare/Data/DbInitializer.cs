using CampusCare.Models;

namespace CampusCare.Data
{
    public static class DbInitializer
    {
        public static void Initialize(ApplicationDbContext context)
        {
            context.Database.EnsureCreated();

            if (context.Complaints.Any())
            {
                return; // DB already has complaints seeded
            }

            var complaints = new Complaint[]
            {
                new Complaint
                {
                    Title = "Projector HDMI Port Damaged",
                    Description = "The HDMI input on the ceiling projector is broken; screens flicker continuously during lectures.",
                    Location = "CSE Block - Seminar Hall 204",
                    CategoryId = 1,
                    Priority = ComplaintPriority.High,
                    Status = ComplaintStatus.InProgress,
                    ReporterName = "Prof. R. Sharma",
                    ReporterEmail = "r.sharma@campus.edu",
                    ReporterPhone = "9876543210",
                    CreatedAt = DateTime.Now.AddDays(-2),
                    AssignedTechnician = "Amit Kumar (IT Dept)",
                    AdminRemarks = "Replacement cable & connector ordered from IT inventory."
                },
                new Complaint
                {
                    Title = "Split AC Leaking Water Heavily",
                    Description = "Unit 2 in the Data Science Lab leaks water over power sockets, causing a tripping hazard.",
                    Location = "Lab 305 (3rd Floor)",
                    CategoryId = 3,
                    Priority = ComplaintPriority.Urgent,
                    Status = ComplaintStatus.Open,
                    ReporterName = "Ananya Patel (Student CR)",
                    ReporterEmail = "ananya.p@student.campus.edu",
                    ReporterPhone = "9823456789",
                    CreatedAt = DateTime.Now.AddHours(-5),
                    AdminRemarks = "Urgent inspection scheduled for today 3 PM."
                },
                new Complaint
                {
                    Title = "Tube Lights Flickering",
                    Description = "Three central tube lights are dead/flickering near the reference section.",
                    Location = "Central Library - 1st Floor",
                    CategoryId = 2,
                    Priority = ComplaintPriority.Low,
                    Status = ComplaintStatus.Resolved,
                    ReporterName = "Library Attendant Ramesh",
                    ReporterEmail = "library@campus.edu",
                    CreatedAt = DateTime.Now.AddDays(-4),
                    UpdatedAt = DateTime.Now.AddDays(-1),
                    AssignedTechnician = "Suresh Verma (Electrician)",
                    AdminRemarks = "Replaced 3 LED batten fixtures. Working normally."
                },
                new Complaint
                {
                    Title = "Restroom Tap Broken and Leaking",
                    Description = "Washbasin tap handle snapped, water running continuously without shutoff.",
                    Location = "Boys Hostel 3 - Ground Floor",
                    CategoryId = 4,
                    Priority = ComplaintPriority.High,
                    Status = ComplaintStatus.Open,
                    ReporterName = "Rahul Verma",
                    ReporterEmail = "rahul.v@student.campus.edu",
                    CreatedAt = DateTime.Now.AddHours(-1)
                },
                new Complaint
                {
                    Title = "Broken Wooden Desk and Bench",
                    Description = "Front row desk in lecture hall has broken support nail and wobbles dangerously.",
                    Location = "Mechanical Block - Room 102",
                    CategoryId = 5,
                    Priority = ComplaintPriority.Medium,
                    Status = ComplaintStatus.Resolved,
                    ReporterName = "Dr. S. Kulkarni",
                    ReporterEmail = "skulkarni@campus.edu",
                    CreatedAt = DateTime.Now.AddDays(-3),
                    UpdatedAt = DateTime.Now.AddHours(-12),
                    AssignedTechnician = "Jagdish (Carpenter)",
                    AdminRemarks = "Joints reinforced with brackets and repainted."
                }
            };

            context.Complaints.AddRange(complaints);
            context.SaveChanges();
        }
    }
}

