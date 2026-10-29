using Microsoft.EntityFrameworkCore;
using CampusCare.Models;

namespace CampusCare.Data
{
    public class ApplicationDbContext : DbContext
    {
        public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options)
            : base(options)
        {
        }

        public DbSet<Complaint> Complaints { get; set; } = null!;
        public DbSet<Category> Categories { get; set; } = null!;

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            base.OnModelCreating(modelBuilder);

            // Configure Relationships
            modelBuilder.Entity<Complaint>()
                .HasOne(c => c.Category)
                .WithMany(cat => cat.Complaints)
                .HasForeignKey(c => c.CategoryId)
                .OnDelete(DeleteBehavior.Restrict);

            // Pre-seed Categories
            modelBuilder.Entity<Category>().HasData(
                new Category { Id = 1, Name = "IT & Audio-Visual", Department = "Computer Center & IT Services", IconClass = "bi-laptop" },
                new Category { Id = 2, Name = "Electrical & Lighting", Department = "Electrical Maintenance", IconClass = "bi-lightning-charge" },
                new Category { Id = 3, Name = "HVAC & Air Conditioning", Department = "Estate & Facility Office", IconClass = "bi-snow" },
                new Category { Id = 4, Name = "Civil & Plumbing", Department = "Civil Works & Sanitation", IconClass = "bi-droplet" },
                new Category { Id = 5, Name = "Furniture & Carpentry", Department = "Workshop & Logistics", IconClass = "bi-wrench-adjustable" }
            );
        }
    }
}

