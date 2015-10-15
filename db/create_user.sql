create database atp;

create user atp idetified by 'atp';

grant all on atp.* to atp;

flush privileges;
