-- pg1.sql

-- This script should load allpredictions.csv into a postgres table.
-- Demo:
-- curl www.spy611.com/csv/allpredictions.csv > /tmp/allpredictions.csv
-- psql -a -P pager=no -f pg1.sql

drop table   allpredictions;
create table allpredictions
(cdate text,cp numeric,pctlead numeric,pctlag1 numeric,pctlag2 numeric,pctlag4 numeric,pctlag8 numeric,pctlag16 numeric,actual_dir numeric,prob_lr numeric,pdir_lr numeric,eff1d_lr numeric,recent_eff_lr numeric,accuracy_lr text,pdir_nb numeric,eff1d_nb numeric,recent_eff_nb numeric,accuracy_nb text,lead numeric,rdelta numeric,gdelta numeric,red numeric,green numeric,allred numeric,allgreen numeric);

COPY allpredictions
(
cdate,cp,pctlead,pctlag1,pctlag2,pctlag4,pctlag8,pctlag16,actual_dir,prob_lr,pdir_lr,eff1d_lr,recent_eff_lr,accuracy_lr,pdir_nb,eff1d_nb,recent_eff_nb,accuracy_nb,lead,rdelta,gdelta,red,green,allred,allgreen
) FROM '/tmp/allpredictions.csv' WITH CSV HEADER DELIMITER AS ','
;

select count(*) from allpredictions;

select min(pctlead), avg(pctlead), max(pctlead) from allpredictions;

-- If pctlag1 is strongly negative, what is pctlead?
select min(pctlead), avg(pctlead), max(pctlead) from allpredictions where pctlag1 < -1.1;

-- If pctlag1 is strongly positive, what is pctlead?
select min(pctlead), avg(pctlead), max(pctlead) from allpredictions where pctlag1 >  1.1;

-- What is correlation between pctlag1, pctlead?
select corr(pctlag1, pctlead) from allpredictions;

-- What did predictions look like in May 2016?
select cdate,cp,pctlead,eff1d_lr,eff1d_nb from allpredictions
where cdate like '2016-05%'
order by cdate
;

-- In May 2016, which worked best, Long-Only, LR, or NB?
-- I should aggregate to find out:
select sum(pctlead),sum(eff1d_lr),sum(eff1d_nb) from allpredictions
where cdate like '2016-05%'
;

