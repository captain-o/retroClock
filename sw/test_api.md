Invoke-RestMethod -Uri "http://localhost:5000/api/setalarm" -Method POST -Headers @{"Content-Type"="application/json"} -Body (@{ "id"=123; "time"="10:30"; "frequency"="weekend" } | ConvertTo-Json)

curl http://localhost:5000/api/alarms | Select-Object -ExpandProperty Content
