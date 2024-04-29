spark-submit \
  --packages za.co.absa.spline.agent.spark:spark-3.2-spline-agent-bundle_2.12:2.0.0 \
  --conf "spark.sql.queryExecutionListeners=za.co.absa.spline.harvester.listener.SplineQueryExecutionListener" \
  --conf "spark.spline.producer.url=http://localhost:8080/producer" \
  code4.py 
