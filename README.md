# AWS-SageMaker



<h2> AWS Comprehend</h2>
<ul>
  <li> AWS comprehend is NLP based service.</li>
  <li> In this repository, I have used S3 bucket to store the file sent, a lambda function which is used for triggering or calling the comprehend's detect_sentiment function.</li>
  <li> Thing to note here is, AWS Comprehend has a max limit of 5000 bytes of input text.</li>
  <li> In order to reduce the size, I have divided the files in the lambda function itself and stored them in the same bucket.</li>
</ul>  
