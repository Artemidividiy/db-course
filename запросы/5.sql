-- Все товары на каждом складе с их типами

select 
	s.name as "stock name", 
	s.longitude as "stock longitude", 
	s.latitude as "stock latitude",  
	i.id as "item id",
	t.name as "item type" 
from stocks s 
left join items i on i.stock = s.id
left join types t on t.id = i.type
order by s.name 