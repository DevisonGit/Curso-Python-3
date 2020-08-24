select 
    regiao as 'Regiao',
    sum(populacao) as total
from `estados`
group by regiao