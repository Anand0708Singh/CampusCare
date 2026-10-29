using Microsoft.EntityFrameworkCore;
using CampusCare.Data;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddControllersWithViews();

// -------------------------------------------------------------
// Database Configuration: MySQL with EF Core (+ In-Memory Fallback)
// -------------------------------------------------------------
var connectionString = builder.Configuration.GetConnectionString("DefaultConnection");
var dbProvider = builder.Configuration.GetValue<string>("DatabaseProvider") ?? "MySQL";

builder.Services.AddDbContext<ApplicationDbContext>(options =>
{
    if (dbProvider.Equals("MySQL", StringComparison.OrdinalIgnoreCase) && !string.IsNullOrEmpty(connectionString))
    {
        try
        {
            var serverVersion = new MariaDbServerVersion(new Version(10, 4, 32));
            options.UseMySql(connectionString, serverVersion, mySqlOptions =>
            {
                mySqlOptions.EnableRetryOnFailure(
                    maxRetryCount: 3,
                    maxRetryDelay: TimeSpan.FromSeconds(5),
                    errorNumbersToAdd: null);
            });
            Console.WriteLine(">>> [DATABASE] Successfully connected to XAMPP MariaDB/MySQL (CampusCareDb)");
        }
        catch (Exception ex)
        {
            Console.WriteLine($">>> [DATABASE ERROR] Falling back to In-Memory: {ex.Message}");
            options.UseInMemoryDatabase("CampusCareDb");
        }
    }
    else
    {
        options.UseInMemoryDatabase("CampusCareDb");
    }
});

// -------------------------------------------------------------
// State Management: Session Setup
// -------------------------------------------------------------
builder.Services.AddDistributedMemoryCache();
builder.Services.AddSession(options =>
{
    options.IdleTimeout = TimeSpan.FromMinutes(30);
    options.Cookie.HttpOnly = true;
    options.Cookie.IsEssential = true;
});

var app = builder.Build();

// Seed initial database records
using (var scope = app.Services.CreateScope())
{
    var services = scope.ServiceProvider;
    try
    {
        var context = services.GetRequiredService<ApplicationDbContext>();
        DbInitializer.Initialize(context);
    }
    catch (Exception ex)
    {
        var logger = services.GetRequiredService<ILogger<Program>>();
        logger.LogError(ex, "An error occurred while seeding the database.");
    }
}

// Configure the HTTP request pipeline.
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Home/Error");
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseRouting();

// Enable Session Middleware
app.UseSession();

app.UseAuthorization();

app.MapStaticAssets();

app.MapControllerRoute(
    name: "default",
    pattern: "{controller=Complaints}/{action=Index}/{id?}")
    .WithStaticAssets();

app.Run();
