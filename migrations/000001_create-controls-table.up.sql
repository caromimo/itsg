CREATE TABLE IF NOT EXISTS controls (
    id SERIAL PRIMARY KEY,
    control TEXT NOT NULL,
    family TEXT NOT NULL,
    name TEXT NOT NULL,
    description TEXT NOT NULL
);