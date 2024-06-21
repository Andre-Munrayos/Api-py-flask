CREATE TABLE contacts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    cellnumber VARCHAR(20) NOT NULL,
    email VARCHAR(100)
);

CREATE INDEX idx_email ON contacts(email);

INSERT INTO contacts (name, cellnumber, email) VALUES
('Laura', '5550201', 'laura.navarro@gmail.com'),
('Messi', '5550202', 'leo.messi@gmail.com'),
('Claudia', '5550203', 'claudia.ramirez@gmail.com'),
('Antonio', '5550204', 'antonio.mendez@gmail.com'),
('Isabel', '5550205', 'isabel.morales@gmail.com'),
('Fernando', '5550206', 'fernando.cruz@gmail.com'),
('Patricia', '5550207', 'patricia.solano@gmail.com'),
('Ricardo', '5550208', 'ricardo.vega@gmail.com'),
('Alejandra', '5550209', 'alejandra.gutierrez@gmail.com'),
('Roberto', '5550210', 'roberto.diaz@gmail.com'),
('Carmen', '5550211', 'carmen.ruiz@gmail.com'),
('Francisco', '5550212', 'francisco.jimenez@gmail.com'),
('Beatriz', '5550213', 'beatriz.fernandez@gmail.com'),
('Alvaro', '5550214', 'alvaro.lopez@gmail.com'),
('Monica', '5550215', 'monica.gonzalez@gmail.com'),
('Pablo', '5550216', 'pablo.martinez@gmail.com'),
('Sara', '5550217', 'sara.perez@gmail.com'),
('David', '5550218', 'david.ortiz@gmail.com'),
('Andrea', '5550219', 'andrea.blanco@gmail.com'),
('Jorge', '5550220', 'jorge.vidal@gmail.com');

select * from contacts