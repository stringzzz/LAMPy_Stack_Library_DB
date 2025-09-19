CREATE DATABASE library_db;
USE library_db;

CREATE TABLE Books (
	Book_ID int not null primary key,
	Title varchar(256) not null, 
	Author varchar(128) not null, 
	Genre varchar(128) not null, 
	Year_Published int not null,
	Pages int not null
);

INSERT INTO Books (Book_ID, Title, Author, Genre, Year_Published, Pages) VALUES 
	(1, 'Martians On Uranus', 'Johnny Williams', 'Science Fiction', 1995, 320),
	(2, 'Terraforming Uranus', 'Johnny Williams', 'Science Fiction', 1996, 345),
	(3, 'Riding The Dragon', 'Michael Marklar', 'Self Help', 1999, 210),
	(4, '1000 Origami Projects', 'Douglas Folder', 'Arts And Crafts', 1993, 500),
	(5, 'The Dragon Goblin', 'Joseph Ritwald', 'Fantasy', 1998, 565),
	(6, 'Sea Of Clams', 'Joseph Ritwald', 'Fantasy', 2000, 390),
	(7, 'The Land Of The Rising Moon', 'Sophia Marklar', 'History', 1995, 454),
	(8, 'The Blossoming Of The Full Moon', 'Sophia Marklar', 'History', 1997, 523),
	(9, 'Shrubs And Trees', 'Daniella Newroot', 'Gardening', 2001, 315),
	(10, 'Astral Presence', 'Jonathan Richards', 'Science Fiction', 2002, 387),
	(11, 'The Long Blade Of The Warrior', 'Clara Voyant', 'Fantasy', 1998, 344),
	(12, 'Dam Those Beavers', 'Mark Rowe', 'Biology', 1985, 213),
	(13, 'Owning The Box', 'Dennis Harman', 'Ethical Hacking', 2008, 137),
	(14, 'Safe Words', 'Kathy Richards', 'Romance', 2003, 456),
	(15, 'Tales From The Relationship', 'Kathy Richards', 'Romance', 2007, 385),
	(16, 'Venus Colliding', 'Johnny Williams', 'Science Fiction', 1999, 376),
	(17, 'Running To The Bathroom', 'Willy Maykit', 'Fiction', 1976, 224),
	(18, 'Toast Whisperer', 'Sally Douglas', 'Cooking', 2002, 185),
	(19, 'Keeping The Log', 'Dennis Harman', 'Computers', 2005, 314),
	(20, 'Tissues For Issues', 'Michael Marklar', 'Self Help', 2003, 180),
	(21, 'The Case Of The Loch Ness', 'Michael Paul', 'Mystery', 1995, 350),
	(22, 'The Missing Number', 'Shigeru Masuda', 'Mystery', 1998, 151),
	(23, 'Splinters Beneath The Nail', 'Freddy Myers', 'Horror', 1982, 298),
	(24, 'The Fall Of Pluto', 'Johnny Williams', 'Science Fiction', 2001, 358),
	(25, 'Rising To The Occasion', 'Sarah Reed', 'Self Help', 2005, 260),
	(26, 'Final Frontier, Or A New Beginning?', 'Neil Kaku', 'Science', 2015, 345),
	(27, 'Breath Of The Demon', 'Carrie Sutherland', 'Horror', 2009, 405),
	(28, 'Picking Peppers', 'Daniella Newroot', 'Gardening', 2005, 387),
	(29, 'Dragon Slayer', 'Charles Temple', 'Fantasy', 1984, 435),
	(30, 'The Mightiest Greenery', 'Chuck Torvalds', 'Gardening', 1975, 420),
	(31, 'Climbing Out Of The Bottle', 'Harry Shelley', 'Self Help', 1998, 342),
	(32, 'The Other Side Of The Mirror', 'Carrie Sutherland', 'Horror', 2011, 436),
	(33, 'The Human Legacy', 'Mark Rowe', 'Biology', 1990, 259),
	(34, 'Defense Against The Dark Arts', 'Dennis Harman', 'Computer Security', 2013, 520),
	(35, 'Dining At The Periodic Table', 'Edward Alphonz', 'Cooking', 2019, 346);			