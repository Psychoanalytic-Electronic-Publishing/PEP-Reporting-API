module.exports = (resource, logicalId) => {
	if (
		logicalId.startsWith('ServerlessDeploymentBucket') ||
		logicalId.startsWith('ApiGatewayResource') ||
		logicalId.startsWith('ApiGatewayRestApi')
	)
		return false;
	else if (logicalId.endsWith('LogGroup')) return { destination: 'LogGroup' };
	else if (logicalId.endsWith('LambdaExecution') || logicalId.endsWith('LambdaFunction'))
		return { destination: 'Lambda' };
	else if (logicalId.startsWith('ApiGatewayMethod')) return { destination: 'ApiGatewayMethod' };
};
