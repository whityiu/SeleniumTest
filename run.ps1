Param(
	[string]$python,
	[string]$tag,
	[switch]$debug
)

$activationScript = $python + '\Scripts\Activate.ps1'

if ($debug) {
	write-output "Activation Script = $activationScript"
}

# Activate the Virtual Environment for Test execution
& $activationScript

# Run the Test discovery & execution script
python run.py -a tags=$tag

# Deactivate the Virtual Environment
deactivate
