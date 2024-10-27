
-- Create Departemen table
CREATE TABLE departemen (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nama_departemen VARCHAR(100) NOT NULL
);

-- Create Jabatan table
CREATE TABLE jabatan (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nama_jabatan VARCHAR(100) NOT NULL
);

-- Create Karyawan table
CREATE TABLE karyawan (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nama_lengkap VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    nomor_telepon VARCHAR(15),
    tanggal_lahir DATE,
    alamat TEXT,
    tanggal_masuk DATE,
    departemen_id INT,
    jabatan_id INT,
    status ENUM('aktif', 'nonaktif') DEFAULT 'aktif',
    FOREIGN KEY (departemen_id) REFERENCES departemen(id) ON DELETE SET NULL,
    FOREIGN KEY (jabatan_id) REFERENCES jabatan(id) ON DELETE SET NULL
);

-- Create Absensi table
CREATE TABLE absensi (
    id INT PRIMARY KEY AUTO_INCREMENT,
    karyawan_id INT,
    tanggal DATE NOT NULL,
    waktu_masuk TIME,
    waktu_keluar TIME,
    status_absensi ENUM('hadir', 'izin', 'sakit', 'alpha') DEFAULT 'hadir',
    FOREIGN KEY (karyawan_id) REFERENCES karyawan(id) ON DELETE CASCADE
);

-- Create Gaji table
CREATE TABLE gaji (
    id INT PRIMARY KEY AUTO_INCREMENT,
    karyawan_id INT,
    bulan VARCHAR(10) NOT NULL,
    gaji_pokok DECIMAL(10,2) DEFAULT 0.00,
    tunjangan DECIMAL(10,2) DEFAULT 0.00,
    potongan DECIMAL(10,2) DEFAULT 0.00,
    total_gaji DECIMAL(10,2) AS (gaji_pokok + tunjangan - potongan) STORED,
    FOREIGN KEY (karyawan_id) REFERENCES karyawan(id) ON DELETE CASCADE
);

-- Insert sample data if needed
-- INSERT INTO departemen (nama_departemen) VALUES ('Finance'), ('HR'), ('IT');
-- INSERT INTO jabatan (nama_jabatan) VALUES ('Manager'), ('Staff'), ('Intern');
