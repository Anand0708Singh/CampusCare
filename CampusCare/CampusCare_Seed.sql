USE CampusCareDb;

CREATE TABLE IF NOT EXISTS Categories (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Department VARCHAR(80) NOT NULL DEFAULT 'General',
    Description VARCHAR(300) NOT NULL,
    DepartmentCode VARCHAR(20) NOT NULL,
    IconClass VARCHAR(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS Complaints (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(100) NOT NULL,
    Description VARCHAR(1000) NOT NULL,
    Location VARCHAR(150) NOT NULL,
    CategoryId INT NOT NULL,
    Priority INT NOT NULL,
    Status INT NOT NULL,
    ReporterName VARCHAR(100) NOT NULL,
    ReporterEmail VARCHAR(100) NOT NULL,
    ReporterPhone VARCHAR(15) NULL,
    CreatedAt DATETIME(6) NOT NULL,
    UpdatedAt DATETIME(6) NULL,
    AssignedTechnician VARCHAR(100) NULL,
    AdminRemarks VARCHAR(500) NULL,
    CONSTRAINT FK_Complaints_Categories_CategoryId FOREIGN KEY (CategoryId) REFERENCES Categories (Id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO Categories (Id, Name, Description, DepartmentCode, IconClass) VALUES
(1, 'IT & Computing Labs', 'Desktop PCs, projectors, network cables, server racks, printers.', 'IT-DEPT', 'bi-laptop'),
(2, 'Electrical & Power', 'Tube lights, fans, power sockets, switchboards, main distribution boards.', 'ELEC-DEPT', 'bi-lightning-charge'),
(3, 'Air Conditioning & HVAC', 'Split AC units, cassette units, HVAC ducting, remote controls.', 'HVAC-DEPT', 'bi-snow'),
(4, 'Furniture & Fixtures', 'Benches, faculty tables, podiums, whiteboards, door locks.', 'MAINT-DEPT', 'bi-easel'),
(5, 'Plumbing & Washrooms', 'Taps, flushes, drainage, water purifiers, washbasins.', 'CIVIL-DEPT', 'bi-droplet')
ON DUPLICATE KEY UPDATE Name=VALUES(Name);

INSERT INTO Complaints (Id, Title, Description, Location, CategoryId, Priority, Status, ReporterName, ReporterEmail, ReporterPhone, CreatedAt, AssignedTechnician, AdminRemarks) VALUES
(1, 'Projector HDMI Port Damaged', 'The HDMI input on the ceiling projector is broken; screens flicker continuously during lectures.', 'CSE Block - Seminar Hall 204', 1, 2, 1, 'Prof. R. Sharma', 'r.sharma@campus.edu', '9876543210', NOW() - INTERVAL 2 DAY, 'Amit Kumar (IT Dept)', 'Replacement cable & connector ordered from IT inventory.'),
(2, 'Split AC Leaking Water Heavily', 'Unit 2 in the Data Science Lab leaks water over power sockets, causing a tripping hazard.', 'Lab 305 (3rd Floor)', 3, 3, 0, 'Ananya Patel (Student CR)', 'ananya.p@student.campus.edu', '9823456789', NOW() - INTERVAL 5 HOUR, NULL, 'Urgent inspection scheduled for today 3 PM.'),
(3, 'Tube Lights Flickering', 'Three central tube lights are dead/flickering near the reference section.', 'Central Library - Reading Hall B', 2, 1, 0, 'Siddharth Dave', 's.dave@campus.edu', '9712345678', NOW() - INTERVAL 1 DAY, NULL, 'Work order generated for electrical technician.'),
(4, 'Faculty Podium Mic Socket Broken', 'The 3.5mm and XLR audio jacks on the podium are loose and emit loud buzzing noises.', 'Classroom 102 (Mechanical Wing)', 1, 2, 2, 'Dr. P. Mehta', 'p.mehta@campus.edu', '9898012345', NOW() - INTERVAL 4 DAY, 'Vikram Rathore', 'Replaced audio socket PCB; tested with wireless microphone.'),
(5, 'Washbasin Tap Constantly Leaking', 'Tap in the 2nd-floor washroom does not close fully, resulting in water wastage.', 'Boys Common Washroom - 2nd Floor', 5, 1, 2, 'Rohan Verma', 'rohan.v@student.campus.edu', '9723451234', NOW() - INTERVAL 6 DAY, 'Ramesh Contractor', 'Replaced rubber washer & valve cartridge.')
ON DUPLICATE KEY UPDATE Title=VALUES(Title);

