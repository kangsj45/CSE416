DROP DATABASE IF EXISTS cse416; -- Temporary code
CREATE DATABASE IF NOT EXISTS cse416 DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci; -- Temporary code
USE cse416; -- Temporary code

GRANT ALL PRIVILEGES ON cse416.* to cse416@localhost IDENTIFIED BY '416final'; -- Temporary code

CREATE TABLE IF NOT EXISTS Account (
  email VARCHAR(100) NOT NULL,
  isAdmin BOOLEAN,
  del VARCHAR(1) DEFAULT 'n',
  PRIMARY KEY (email)
) ENGINE=INNODB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS AdminAccount (
  email VARCHAR(100) NOT NULL,
  password VARCHAR(100) NOT NULL,
  name VARCHAR(100) NOT NULL,
  profilePictureURL VARCHAR(65535),
  PRIMARY KEY (email),
  FOREIGN KEY (email) REFERENCES Account(email) ON DELETE CASCADE
) ENGINE=INNODB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS UserAccount (
  email VARCHAR(100) NOT NULL,
  password VARCHAR(100) NOT NULL,
  name VARCHAR(100) NOT NULL,
  profilePictureURL VARCHAR(65535),
  PRIMARY KEY (email),
  FOREIGN KEY (email) REFERENCES Account(email) ON DELETE CASCADE
) ENGINE=INNODB DEFAULT CHARSET=utf8;

/*
CREATE TABLE IF NOT EXISTS SendFriendRequest (
  senderID VARCHAR(50) NOT NULL,
  receiverID VARCHAR(50) NOT NULL,
  PRIMARY KEY (senderID, receiverID),
  FOREIGN KEY (senderID) REFERENCES UserAccount(userID) ON DELETE NO ACTION,
  FOREIGN KEY (receiverID) REFERENCES UserAccount(userID) ON DELETE NO ACTION
) ENGINE=INNODB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS IsFriendWith (
  userID VARCHAR(50) NOT NULL,
  friendID VARCHAR(50) NOT NULL,
  PRIMARY KEY (userID, friendID),
  FOREIGN KEY (userID) REFERENCES UserAccount(userID) ON DELETE NO ACTION,
  FOREIGN KEY (friendID) REFERENCES UserAccount(userID) ON DELETE NO ACTION
) ENGINE=INNODB DEFAULT CHARSET=utf8;

*/

CREATE TABLE IF NOT EXISTS HasSearchHistory (
  email VARCHAR(100) NOT NULL,
  idx INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
  word VARCHAR(100) NOT NULL,
  regDate DATETIME NOT NULL,
  FOREIGN KEY (email) REFERENCES UserAccount(email) ON DELETE NO ACTION
) ENGINE=INNODB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS HasSourceOrder (
  email VARCHAR(100) NOT NULL,
  order INTEGER NOT NULL,
  source VARCHAR(500) NOT NULL,
  PRIMARY KEY (email, order),
  FOREIGN KEY (email) REFERENCES UserAccount(email) ON DELETE NO ACTION
) ENGINE=INNODB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `packages`;
CREATE TABLE `packages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `words`;
CREATE TABLE `words` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `pos` varchar(45) DEFAULT NULL,
  `meaning` longtext,
  `image` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `sets`;
CREATE TABLE `sets` (
  `p_id` int(11) NOT NULL,
  `w_id` int(11) NOT NULL,
  PRIMARY KEY (`p_id`,`w_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*
CREATE TABLE IF NOT EXISTS CardPackage (
  packageID VARCHAR(50) NOT NULL,
  packageTitle VARCHAR(500) NOT NULL,
  PRIMARY KEY (packageID)
) ENGINE=INNODB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS HasCardPackage (
  userID VARCHAR(50) NOT NULL,
  packageID VARCHAR(50) NOT NULL,
  PRIMARY KEY (userID, packageID),
  FOREIGN KEY (userID) REFERENCES UserAccount(userID) ON DELETE NO ACTION,
  FOREIGN KEY (packageID) REFERENCES CardPackage(packageID) ON DELETE CASCADE
) ENGINE=INNODB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS ShareOption (
  ownerUserID VARCHAR(50) NOT NULL,
  packageID VARCHAR(50) NOT NULL,
  shareOptionID VARCHAR(50) NOT NULL,
  PRIMARY KEY (shareOptionID),
  FOREIGN KEY (userID) REFERENCES UserAccount(userID) ON DELETE NO ACTION,
  FOREIGN KEY (packageID) REFERENCES CardPackage(packageID) ON DELETE NO ACTION
) ENGINE=INNODB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS HasShareList (
  shareOptionID VARCHAR(50) NOT NULL,
  userID VARCHAR(50) NOT NULL,
  accessType VARCHAR(10) NOT NULL,
  PRIMARY KEY (shareOptionID, userID)
  FOREIGN KEY (shareOptionID) REFERENCES ShareOption(shareOptionID) ON DELETE NO ACTION,
  FOREIGN KEY (userID) REFERENCES UserAccount(userID) ON DELETE NO ACTION,
) ENGINE=INNODB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS NoteCard (
  noteCardID VARCHAR(50) NOT NULL,
  title VARCHAR(500),
  definition VARCHAR(65535),
  partOfSpeech VARCHAR(65535),
  photoURL VARCHAR(65535),
  videoURL VARCHAR(65535),
  PRIMARY KEY (noteCardID)
) ENGINE=INNODB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS HasNoteCard (
  packageID VARCHAR(50) NOT NULL,
  noteCardID VARCHAR(50) NOT NULL,
  PRIMARY KEY (packageID, noteCardID)
  FOREIGN KEY (packageID) REFERENCES CardPackage(packageID) ON DELETE NO ACTION,
  FOREIGN KEY (notecardID) REFERENCES NoteCard(noteCardID) ON DELETE CASCADE
) ENGINE=INNODB DEFAULT CHARSET=utf8;

*/

CREATE TABLE IF NOT EXISTS Challenge (
  challengeID VARCHAR(50) NOT NULL,
  totalScore FLOAT NOT NULL,
  maximumTime FLOAT NOT NULL
  PRIMARY KEY (challengeID)
) ENGINE=INNODB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS GenerateChallenge (
  creatorID VARCHAR(50),
  challengeID VARCHAR(50) NOT NULL,
  dateCreated DATE, -- changed the variable name as date is a datatype in MySQL
  PRIMARY KEY (adminID, challengeID),
  FOREIGN KEY (creator) REFERENCES AdminAccount(userID) ON DELETE NO ACTION,
  FOREIGN KEY (challengeID) REFERENCES Challenge(challengeID) ON DELETE CASCADE
) ENGINE=INNODB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS TakeChallenge (
  userID VARCHAR(50) NOT NULL,
  challengeID VARCHAR(50) NOT NULL,
  score FLOAT,
  timeTaken FLOAT NOT NULL,
  PRIMARY KEY (userID, challengeID),
  FOREIGN KEY (userID) REFERENCES UserAccount(userID) ON DELETE NO ACTION,
  FOREIGN KEY (challengeID) REFERENCES Challenge(challengeID) ON DELETE NO ACTION
) ENGINE=INNODB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS HasChallengeRanking (
  challengeID VARCHAR(50) NOT NULL,
  userID VARCHAR(50) NOT NULL,
  rank INTEGER NOT NULL,
  score FLOAT,
  timeTaken FLOAT NOT NULL,
  PRIMARY KEY (challengeID, userID),
  FOREIGN KEY (challengeID) REFERENCES Challenge(challengeID) ON DELETE NO ACTION,
  FOREIGN KEY (userID) REFERENCES UserAccount(userID) ON DELETE NO ACTION,
  FOREIGN KEY (score) REFERENCES TakeChallenge(score) ON DELETE CASCADE,
  FOREIGN KEY (timeTaken) REFERENCES TakeChallenge(timeTaken) ON DELETE CASCADE
) ENGINE=INNODB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS Problem (
  problemID VARCHAR(50) NOT NULL,
  problem VARCHAR(500) NOT NULL,
  answer INTEGER NOT NULL,
  firstChoice VARCHAR(300),
  secondChoice VARCHAR(300),
  thirdChoice VARCHAR(300),
  fourthChoice VARCHAR(300),
  selected VARCHAR(300) NOT NULL,
  PRIMARY KEY (problemID)
) ENGINE=INNODB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS HasChallengeProblem (
  challengeID VARCHAR(50) NOT NULL,
  problemID VARCHAR(50) NOT NULL,
  PRIMARY KEY (challengeID, problemID)
  FOREIGN KEY (challengeID) REFERENCES Challenge(challengeID) ON DELETE NO ACTION,
  FOREIGN KEY (problemID) REFERENCES Problem(problemID) ON DELETE CASCADE
) ENGINE=INNODB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS Quiz (
  quizID VARCHAR(50) NOT NULL,
  totalNumberOfQuestions INTEGER NOT NULL,
  dateCreated DATE NOT NULL, -- changed the variable name as date is a datatype in MySQL
  PRIMARY KEY (quizID)
) ENGINE=INNODB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS HasQuizHistory (
  userID VARCHAR(50) NOT NULL,
  quizID VARCHAR(50) NOT NULL,
  completedDateTime TIMESTAMP NOT NULL,
  numberOfCorrectAnswers INTEGER,
  numberOfIncorrectAnswers INTEGER,
  PRIMARY KEY (userID, quizID, order),
  FOREIGN KEY (userID) REFERENCES UserAccount(userID) ON DELETE NO ACTION,
  FOREIGN KEY (quizID) REFERENCES Quiz(quizID) ON DELETE NO ACTION
) ENGINE=INNODB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS HasQuizProblem (
  quizID VARCHAR(50) NOT NULL,
  problemID VARCHAR(50) NOT NULL,
  PRIMARY KEY (quizID, problemID)
  FOREIGN KEY (quizID) REFERENCES Quiz(quizID) ON DELETE NO ACTION,
  FOREIGN KEY (problemID) REFERENCES Problem(problemID) ON DELETE CASCADE
) ENGINE=INNODB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS GenerateQuiz (
  userID VARCHAR(50) NOT NULL,
  packageID VARCHAR(50) NOT NULL,
  quizID VARCHAR(50) NOT NULL,
  PRIMARY KEY (userID, packageID, quizID)
  FOREIGN KEY (userID) REFERENCES UserAccount(userID) ON DELETE NO ACTION,
  FOREIGN KEY (packageID) REFERENCES CardPackage(packageID) ON DELETE NO ACTION,
  FOREIGN KEY (quizID) REFERENCES Quiz(quizID) ON DELETE CASCADE
)  ENGINE=INNODB DEFAULT CHARSET=utf8;
