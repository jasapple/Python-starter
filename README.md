# New Script #

Starter for new Python Scripts


## Background ##

For many of my python scripts, I utilize the ArgParse and Logging libraries and I was tired of rewriting the same starter code for my scripts, so I made this template.
	
ArgParse was preferred as most deployment environments, we can control added arguments in a programmatic way as well as quick CLI testing

<TODO> add config file feature

Logging levels is ideal when using a logging aggregation platform; such as the ELK Stack, Splunk, or AWS CloudWatch.

Timestamp follows [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. Time is UTC (see [script.py#L11](https://github.com/jasapple/Python-starter/blob/main/script.py#L11))
