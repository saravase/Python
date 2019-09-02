$(function(){
   $(window).resize(function(){
    if($(window).width() <= 770 && !$("#wrapper").hasClass('toggled')){
    	$("#wrapper").addClass("toggled");
    }else if($("#wrapper").hasClass('toggled')){
    	$("#wrapper").removeClass("toggled");
    }
}); 

   $('.card .card-body .text-truncate').hover(function(){
   		$(this).attr('title', $(this).text());
   		$(this).css({
   			'cursor':'pointer'
   		});
   });

   $('.card').addClass('hoverable');

   let states = [
  "Alabama",
  "Alaska",
  "Arizona",
  "Arkansas",
  "California",
  "Colorado",
  "Connecticut",
  "Delaware",
  "Florida",
  "Georgia",
  "Hawaii",
  "Idaho",
  "Illnois",
  "Indiana",
  "Iowa",
  "Kansas",
  "Kentucky",
  "Louisiana",
  "Maine",
  "Maryland",
  "Massachusetts",
  "Michigan",
  "Minnesota",
  "Mississippi",
  "Missouri",
  "Montana",
  "Nebraska",
  "Nevada",
  "New Hampshire",
  "New Jersey",
  "New Mexico",
  "New York",
  "North Carolina",
  "North Dakota",
  "Ohio",
  "Oklahoma",
  "Oregon",
  "Pennsylvania",
  "Rhode Island",
  "South Carolina",
  "South Dakota",
  "Tennessee",
  "Texas",
  "Utah",
  "Vermont",
  "Virginia",
  "Washington",
  "West Virginia",
  "Wisconsin",
  "Wyoming"
];

  $('#chips-autocomplete-test').materialChip({
    placeholder: 'Enter a tag',
    secondaryPlaceholder: '+Tag',
    dataChip: states
  });
});