create database atp;

create user atp identified by 'atp';

grant all on atp.* to atp;

flush privileges;
