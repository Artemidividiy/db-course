-- все склады Cент-Люсии 
select s.name, 
 	s.longitude, 
 	s.latitude, 
 	countries.name as "country name" 
from stocks s 
left join countries on countries.id = s.country 
where countries.name = 'Saint Lucia'

