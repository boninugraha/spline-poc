spark-submit \
  --packages za.co.absa.spline.agent.spark:spark-3.0-spline-agent-bundle_2.12:2.0.0 \
  --conf "spark.sql.queryExecutionListeners=za.co.absa.spline.harvester.listener.SplineQueryExecutionListener" \
  --conf "spark.spline.producer.url=http://localhost:8081/producer" \
  code.py 