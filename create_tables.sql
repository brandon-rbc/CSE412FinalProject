CREATE TABLE "user" (
  userID INTEGER NOT NULL,
  age INTEGER,
  username VARCHAR(100),
  gender CHAR(1),
  PRIMARY KEY(userID),
  CHECK (age<120)
);

CREATE TABLE "director" (
  directorID INTEGER NOT NULL,
  name VARCHAR(100),
  dateOfBirth DATE,
  dateOfDeath DATE,
  PRIMARY KEY(directorID)
);

CREATE TABLE "mediaObject" (
  mediaID INTEGER NOT NULL,
  name VARCHAR(100),
  synopsis VARCHAR(255),
  year INTEGER,
  poster_url VARCHAR(2000),
  genres VARCHAR[],
  rating NUMERIC,
  PRIMARY KEY(mediaID)
);

CREATE TABLE "show" (
  mediaID INTEGER,
  numSeasons INTEGER,
  numEpisodes INTEGER,
  PRIMARY KEY(mediaID),
  FOREIGN KEY(mediaID) REFERENCES "mediaObject" ON DELETE CASCADE
);

CREATE TABLE "movie" (
  mediaID INTEGER,
  runtime INTEGER,
  PRIMARY KEY(mediaID),
  FOREIGN KEY(mediaID) REFERENCES "mediaObject" ON DELETE CASCADE
);

CREATE TABLE "directs" (
  directorID INTEGER,
  mediaID INTEGER,
  PRIMARY KEY(directorID, mediaID),
  FOREIGN KEY(directorID) REFERENCES "director" ON DELETE CASCADE,
  FOREIGN KEY(mediaID) REFERENCES "mediaObject" ON DELETE CASCADE
);

CREATE TABLE "favoritedBy" (
  userID INTEGER,
  mediaID INTEGER,
  dateAdded DATE,
  PRIMARY KEY(userID, mediaID),
  FOREIGN KEY(userID) REFERENCES "user" ON DELETE CASCADE,
  FOREIGN KEY(mediaID) REFERENCES "mediaObject" ON DELETE CASCADE
);
