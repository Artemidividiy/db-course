-- все товары, страна отправки которых совпадает со страной, где находятся их склады хранения

select distinct 
	i.id as "item id", 
	i.name, 
	t.name as "type", 
	o.name as "organization", 
	c.name as "country",
	i.arrival_date 
	from items i 
	left join types t on t.id = i.type 
	left join places p on p.id = i."point of departure" 
	left join countries c on c.id = i."point of departure"
	left join organizations o on p."Organization" = o.id
	inner join stocks s on s.country = i."point of departure"

order by "item id"