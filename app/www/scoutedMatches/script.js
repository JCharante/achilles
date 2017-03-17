Vue.component('match', {
	props: ['match'],
	methods: {
		viewQrCode: function() {
			var self = this;
			var packed_json_string = JSONC.pack(self.match);
			cordova.plugins.barcodeScanner.encode(cordova.plugins.barcodeScanner.Encode.TEXT_TYPE, packed_json_string, function(success) {
					console.log(success);
				}, function(fail) {
					toast('error', 'Error', 'Generating QR Code Failed');
					console.log(fail);
				}
			);
		}
	},
	computed: {
		linkToMatch: function() {
			var self = this;
			return '../scout_match/index.html?match_id=' + self.match.match_id;
		},
		eventName: function() {
			var self = this;
			var name = null;
			switch (self.match.event_name) {
				case 'greater-boston':
					name = 'Greater Boston';
					break;
				case 'pine-tree':
					name = 'Pine Tree';
					break;
				default:
					name = self.match.event_name;
					break;
			}
			return name;
		}
	},
	template:
	'<div class="col-lg4 col-md-6 col-xs-12">' +
		'<div class="panel panel-default">' +
			'<div class="panel-heading">' +
				'<p>{{ eventName }} - {{ match.match_number }}</p>' +
			'</div>' +
			'<div class="panel-body">' +
				'<a class="btn btn-primary" :href="linkToMatch" role="button">View Match</a>' +
				'<a class="btn btn-default" v-on:click="viewQrCode" role="button">View QR Code</a>' +
			'</div>' +
		'</div>' +
	'</div>'
});


function onceDocumentReady() {
	var scouted_matches = new Vue({
		el: '#vue-app',
		mounted: function() {
			var self = this;
			self.scoutedMatches = JSON.parse(localStorage.getItem('matches') || '{}')
		},
		data: function () {
			return {
				scoutedMatches: {}
			}
		}
	})
}

$(document).ready(onceDocumentReady);