{{- define "hello-chart.name" -}}
{{ .Chart.Name }}
{{- end }}

{{- define "hello-chart.fullname" -}}
{{ .Release.Name }}-{{ .Chart.Name }}
{{- end }}