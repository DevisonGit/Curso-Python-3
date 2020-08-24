insert into empresas(nome, cnpj)
values
    ('Bradesco', 06170198000138),
    ('Vale', 95815827000160),
    ('Cielo', 80087823000135);


-- alter table empresas modify cnpj varchar(14)

-- desc empresas;

select * from empresas;
select * from cidades;
select * from empresas_unidades;

insert into empresas_unidades (empresa_id, cidade_id, sede)
values
    (1, 3, 1),
    (1, 6, 0),
    (2, 6, 1),
    (2, 3, 0);
