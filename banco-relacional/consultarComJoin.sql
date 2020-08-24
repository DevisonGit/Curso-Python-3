select * from `estados` as c, cidades as a
where c.id = a.estado_id


select 
    c.nome as Cidade,
    e.nome as Estado
from `estados` as e
inner join cidades as c
on e.id = c.estado_id
