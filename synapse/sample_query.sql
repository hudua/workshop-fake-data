select x.SIN, approved, FLOOR(DATEDIFF(DAY, y.DateOfBirth, GETDATE()) / 365.25) AS AGE, avg(ApplicationCost) avgcost from esdc.dbo.applications x 
join esdc.dbo.people y 
    on x.SIN = y.SIN 
join esdc.dbo.social_programs z 
    on x.programID = z.programID

group by x.SIN, approved, y.DateOfBirth
