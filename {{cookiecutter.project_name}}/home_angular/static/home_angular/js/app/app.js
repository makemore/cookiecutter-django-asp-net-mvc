var angularApp = angular.module('angularApp', ['ui.router']);

angularApp.config(function($stateProvider, $urlRouterProvider) {
    
    $urlRouterProvider.otherwise('/');
    
    $stateProvider
        
        // HOME STATES AND NESTED VIEWS ========================================
        .state('root', {
            abstract: true,
            views: {
                'header': {
                    templateUrl: '/static/home_angular/js/app/root/header.html',
                    controller: ['$scope',
                        function ($scope) {

                        }]
                }
            }
        })

        .state('root.home', {
            url: '/',
            views: {
              'container@': {
                  templateUrl: '/static/home_angular/js/app/home/home.html',
            controller: ['$scope',
                        function ($scope) {

                        }]
                    }
                }
        })
        
        // ABOUT PAGE AND MULTIPLE NAMED VIEWS =================================
        .state('root.about', {
            url: '/about',
             views: {
                 'container@': {
                     templateUrl: '/static/home_angular/js/app/about/about.html',
                     controller: ['$scope',
                         function ($scope) {

                         }]
                 }
             }
        });
        
});
