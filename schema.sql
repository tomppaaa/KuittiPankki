CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    password TEXT,
    role INTEGER
);

CREATE TABLE receipts (
    id SERIAL PRIMARY KEY,
    creator_id INTEGER REFERENCES users,
    shop_id INTEGER REFERENCES ,
    date_issued DATE
);

CREATE TABLE shops (
    id SERIAL PRIMARY KEY,
    shop_name TEXT,
    type TEXT
    CONSTRAINT shop_name_unique UNIQUE (shop_name)
);

CREATE TABLE products(
    id SERIAL PRIMARY KEY,
    receipt_id INTEGER REFERENCES receipts,
    price INTEGER,
    calories INTEGER,
    type TEXT
);

CREATE TABLE stats (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    receipt_id INTEGER REFERENCES receipts,
    total_price INTEGER,
    total_calories INTEGER
);