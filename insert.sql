INSERT INTO core_user (id, email, phone_number, password)
VALUES ('2d94a60b-5a5e-4c7e-a424-72e74b1c4c93', 'user1@example.com', '1234567890', 'password1'),
       ('168287a3-f3d8-4ba4-92e4-1d4be4777a14', 'user2@example.com', '9876543210', 'password2');

INSERT INTO core_post (id, publisher_id, category, title, description, requirements, salary, contact_name, phone_number, email, created_at)
VALUES ('08a07d62-66da-40d2-84ef-2db28e6fb69a', '2d94a60b-5a5e-4c7e-a424-72e74b1c4c93', 'Category1', 'Post Title 1', 'Post Description 1', 'Post Requirements 1', '1000', 'Contact Name 1', '111-111-1111', 'email1@example.com', now()),
       ('ff32e65d-1ef1-484d-bd46-0cc4f4cc8667', '2d94a60b-5a5e-4c7e-a424-72e74b1c4c93', 'Category2', 'Post Title 2', 'Post Description 2', 'Post Requirements 2', '2000', 'Contact Name 2', '222-222-2222', 'email2@example.com', now()),
       ('f9d6977a-22d4-4c2b-a17d-f6187a2d06c0', '2d94a60b-5a5e-4c7e-a424-72e74b1c4c93', 'Category1', 'Post Title 3', 'Post Description 3', 'Post Requirements 3', '3000', 'Contact Name 3', '333-333-3333', 'email3@example.com', now()),
       ('92060f34-8e64-4d88-87fc-9182b295ca78', '168287a3-f3d8-4ba4-92e4-1d4be4777a14', 'Category2', 'Post Title 4', 'Post Description 4', 'Post Requirements 4', '4000', 'Contact Name 4', '444-444-4444', 'email4@example.com', now()),
       ('24320827-cd68-4b67-bf25-dabbe83dcd7d', '168287a3-f3d8-4ba4-92e4-1d4be4777a14', 'Category1', 'Post Title 5', 'Post Description 5', 'Post Requirements 5', '5000', 'Contact Name 5', '555-555-5555', 'email5@example.com', now()),

