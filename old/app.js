/**
 * File: app.js
 * Author: Zachary Liou
 * Date Created: 2016 June 27
 */

(function() {
    'use strict';

    angular
        .module('app', [])
    	.controller('MainCtrl', MainCtrl)
    	.factory('memberService');



// Controller ////////

	/**
	 * @param memberService
	 */
    function MainCtrl(memberService) {

    	var vm = this;

    	var members = [];

    	members = memberService.getNames();


    }


// Factory ////////


	function memberService() {

		var names = ["hello"];

		return {
			getNames: function() {
				console.log(names);
				return names;
			}
		}

	}


    
})();