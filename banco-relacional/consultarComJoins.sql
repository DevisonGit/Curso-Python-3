select * from wm.cidades;
select * from wm.prefeitos;

select * 
from wm.cidades c 
inner join wm.prefeitos p 
on c.id = p.cidade_id;

select * 
from wm.cidades c 
left join wm.prefeitos p
on c.id = p.cidade_id;

select *
from wm.cidades c
right join wm.prefeitos p
on c.id = p.cidade_i;