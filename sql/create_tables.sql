CREATE TABLE api_users (
    id INTEGER PRIMARY KEY,
    name VARCHAR(80),
    username VARCHAR(100),
    email VARCHAR(150),
    phone VARCHAR(15),
    website VARCHAR(100),
    city VARCHAR(150),
    company_name VARCHAR(200),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS pipeline_audit (
    run_id SERIAL PRIMARY KEY,
    pipeline_name VARCHAR(100),
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    records_extracted INTEGER,
    records_loaded INTEGER,
    status VARCHAR(50),
    error_message TEXT
);