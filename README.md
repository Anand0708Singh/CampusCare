# 🛡️ CampusCare: Smart Campus Facility & Grievance Management System

[![ASP.NET Core](https://img.shields.io/badge/ASP.NET%20Core-10.0-512BD4?logo=dotnet&logoColor=white)](https://dotnet.microsoft.com/)
[![EF Core](https://img.shields.io/badge/EF%20Core-Pomelo%20MySQL-00758F?logo=mysql&logoColor=white)](https://github.com/PomeloFoundation/Pomelo.EntityFrameworkCore.MySql)
[![Bootstrap](https://img.shields.io/badge/UI-Bootstrap%205.3-7952B3?logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![Poster Deliverable](https://img.shields.io/badge/Poster-A2%20Print%20Ready-0284C7)](#-a2-technical-poster)

> An enterprise-grade Web Technologies with .NET course project delivering an end-to-end collegiate equipment breakdown and facilities grievance tracking portal.

---

## 👨‍🎓 Candidate & Academic Information

- **Student Name:** Singh Anand Rajkishor
- **Enrollment No:** 202403103510368
- **Department:** B.Tech Computer Science & Engineering (Cyber Security)
- **Division:** 5F
- **Institute:** Asha M. Tarsadia Institute of Computer Science and Technology (AMTICS)
- **University:** Uka Tarsadia University (UTU)
- **Course:** Web Technologies with .NET (Course Code: WTN)

---

## 🌟 Key Application Features

- **Centralized Issue Lodging:** Students and faculty report facility defects (projectors, split ACs, power outlets, plumbing) with room locations, urgency levels, and contact details in < 60 seconds.
- **Admin Control Desk:** Real-time dashboard to filter grievances by department, assign technicians, update remarks, and progress ticket lifecycle (`Open` ➔ `InProgress` ➔ `Resolved` ➔ `Closed`).
- **Operational SLA Analytics:** High-level dashboard computing total complaints, active workloads, resolution percentages, and departmental breakdown charts.
- **Automated MySQL Pre-Seeding:** Pre-populates 5 campus facilities categories and realistic sample grievances on startup.
- **Fail-Safe In-Memory Fallback:** Resilient dual-database engine that gracefully falls back to EF Core In-Memory storage if MySQL daemon is paused.

---

## 🏗️ Architecture & .NET Core Implementations

| # | Core Concept | Implementation in CampusCare | Source Reference |
|---|---|---|---|
| **1** | **MVC Architectural Pattern** | Decoupled entities, Razor UI views, and controllers with Dependency Injection | `Models/`, `Views/`, `Controllers/` |
| **2** | **EF Core Code-First ORM** | Schema migrations and relational MySQL mapping via `Pomelo.EntityFrameworkCore.MySql` | `Data/ApplicationDbContext.cs` |
| **3** | **Complete CRUD Operations** | Asynchronous Create, Read, Update, Delete with confirmation modals and SLA reporting | `ComplaintsController.cs` |
| **4** | **Form Handling & Anti-CSRF** | Strongly-typed model bindings with Tag Helpers (`asp-for`, `asp-items`) and `[ValidateAntiForgeryToken]` | `Views/Complaints/Create.cshtml` |
| **5** | **Model Validation** | Dual-layer validation: server-side `DataAnnotations` + client-side jQuery Unobtrusive | `Models/Complaint.cs` |
| **6** | **State Management** | Post-Redirect-Get (PRG) pattern utilizing `TempData["SuccessMessage"]` dismissible toasts | `ComplaintsController.cs` |
| **7** | **Responsive Design** | 12-column mobile-first Bootstrap 5 grid layout with KPI summary cards | `Views/Shared/_Layout.cshtml` |

---

## 🚀 Getting Started

### Prerequisites
- [.NET SDK 10.0](https://dotnet.microsoft.com/download)
- [XAMPP](https://www.apachefriends.org/) (Apache + MySQL running on port 3306)

### 1. Database Setup (MySQL / XAMPP)
Start MySQL in your XAMPP Control Panel. The app automatically creates and seeds `CampusCareDb`.  
You can also import the provided SQL script:
```powershell
& 'C:\xampp\mysql\bin\mysql.exe' -u root -e "CREATE DATABASE IF NOT EXISTS CampusCareDb;"
& 'C:\xampp\mysql\bin\mysql.exe' -u root CampusCareDb -e "source CampusCare/CampusCare_Seed.sql"
```

### 2. Configure Connection String
Verify `CampusCare/appsettings.json`:
```json
"ConnectionStrings": {
  "DefaultConnection": "Server=localhost;Port=3306;Database=CampusCareDb;User=root;Password=;"
},
"DatabaseProvider": "MySQL"
```

### 3. Run the Application
```powershell
cd CampusCare
dotnet run
```
Open your browser and navigate to:
👉 **`http://localhost:5000`** (or **`http://localhost:5000/Complaints`**)

---

## 🎨 A2 Technical Poster

The repository includes the finalized technical presentation poster designed to exact **A2 portrait dimensions (420 × 594 mm)**:
- **Vector PDF:** [`poster/CampusCare - A2 Project Poster.pdf`](poster/CampusCare%20-%20A2%20Project%20Poster.pdf)
- **High-Res Visual Preview:** [`poster/CampusCare_A2_Poster_Preview.png`](poster/CampusCare_A2_Poster_Preview.png)
- **Web Source & One-Click Print Utility:** [`poster/index.html`](poster/index.html)
- **Automated Generation Script:** [`poster/generate_poster_pdf.py`](poster/generate_poster_pdf.py)

---

## 📁 Repository Structure

```
├── CampusCare/                    # ASP.NET Core MVC Application
│   ├── Controllers/               # ComplaintsController (CRUD & Analytics)
│   ├── Data/                      # ApplicationDbContext & DbInitializer
│   ├── Models/                    # Complaint, Category, Enums, ViewModels
│   ├── Views/                     # Razor Views (Index, Create, Edit, Delete, Analytics)
│   ├── wwwroot/                   # Bootstrap 5, Icons, jQuery scripts & styles
│   ├── appsettings.json           # MySQL connection configurations
│   ├── CampusCare_Seed.sql        # Standalone MySQL schema and seed data
│   └── Program.cs                 # Middleware, DI, EF Core & Session setup
├── poster/                        # A2 Technical Presentation Poster
│   ├── CampusCare - A2 Project Poster.pdf  # Finalized print-ready vector PDF
│   ├── CampusCare_A2_Poster_Preview.png    # High-resolution visual render
│   ├── index.html                 # Interactive web preview & print interface
│   ├── generate_poster_pdf.py     # Python ReportLab vector PDF generator
│   ├── utu logo.jpg               # Institutional Logo (Left)
│   └── amtics logo.png            # Institutional Logo (Right)
├── .gitignore                     # Optimized exclusion rules
└── README.md                      # Project documentation
```

---

## 📜 License
Developed as an academic submission for the **Web Technologies with .NET** curriculum at **AMTICS, Uka Tarsadia University**.
