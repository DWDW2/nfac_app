create table if not exists events(
    id integer primary key autoincrement,
    title text not null, 
    descript text not null, 
    url_to_img text not null,
    date_event date not null
);