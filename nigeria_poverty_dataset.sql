/*
select country , year ,reporting_level , headcount_ratio_international_povline from pip_dataset
where reporting_level='national' and country='nigeria';
*/

select country  ,year, AVG(headcount_ratio_international_povline) as average_pov from pip_dataset 
 where reporting_level='national' and country='nigeria'  group by country ,year; 
 
 



