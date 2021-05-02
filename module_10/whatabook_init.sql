/*
    Joey Spielman| Whatabook init file| 05/02/21
*/
DROP USER IF EXISTS 'whatabook_user'@'localhost';

CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;
CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);

CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

INSERT INTO store(locale)
    VALUES('617 South Denver, Hastings, NE 68901');

INSERT INTO book(book_name, author, details)
    VALUES('Ayoade on Ayoade', 'Richard Ayoade', 'A cinematic odyssey');

INSERT INTO book(book_name, author, details)
    VALUES('Twilight Falling', 'Paul S. Kemp', 'First book fo the Erevis Cale series');

INSERT INTO book(book_name, author, details)
    VALUES('Super Mario', 'Jeff Ryan', 'How Nintendo conquered America');

INSERT INTO book(book_name, author, details)
    VALUES('Ayoade on Ayoade', 'Richard Ayoade', 'A cinematic odyssey');

INSERT INTO book(book_name, author, details)
    VALUES('How to Ruin Everything', 'George Watsky', 'Essays from life');

INSERT INTO book(book_name, author, details)
    VALUES('Cracking the Coding Interview', 'Gayle McDowell', 'Interview Practice');

INSERT INTO book(book_name, author, details)
    VALUES('The Way of Kings', 'Brandon Sanderson', 'First book fo the Stormlight Archive');

INSERT INTO book(book_name, author, details)
    VALUES('The Crystal Shard', 'R.A. Salvatore', 'Spine of the World Series');

INSERT INTO book(book_name, author, details)
    VALUES('American Gods', 'Neil Gaiman', 'Fantasy');

INSERT INTO user(first_name, last_name) 
    VALUES('Gus', 'Gusserson');
INSERT INTO user(first_name, last_name) 
    VALUES('Penny', 'Jane');
INSERT INTO user(first_name, last_name) 
    VALUES('Sophie', 'Reams');

INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Gus'), 
        (SELECT book_id FROM book WHERE book_name = 'Super Mario')
    );
INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Penny'), 
        (SELECT book_id FROM book WHERE book_name = 'How to Ruin Everything')
    );    
INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Sophie'), 
        (SELECT book_id FROM book WHERE book_name = 'American Gods')
    );