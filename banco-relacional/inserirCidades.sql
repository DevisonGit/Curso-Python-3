insert into cidades (nome, area, estado_id)
values ('Campinas', 795, 21)


SELECT * from cidades


insert into cidades (nome, area, estado_id)
values (
    'Caruaru',
    920.6,
    (select id from `estados` where sigla = 'PE')
)


delete from cidades where id = 8