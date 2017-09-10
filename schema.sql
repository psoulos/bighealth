create table Diary (
    id integer primary key autoincrement,
    userId integer not null,
    date_ text not null,
    timeIntoBed text not null,
    timeOutOfBed text not null,
    sleepQuality integer not null
);