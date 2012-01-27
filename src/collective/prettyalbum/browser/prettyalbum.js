(function($) {

    $(document).ready(function() {
        $('a.prettyAlbum').bind('click', function(event) {
            event.preventDefault();
            var url = $(this).attr('href');
            if ( url.substr(-1) === "/" ) {
                url += '@@prettyalbum_json_data';
            } else {
                url += '/@@prettyalbum_json_data';
            }
            $.getJSON(url, function(data) {
                $.prettyPhoto.open(data.images, data.titles, data.descriptions);
            });
        });
        
        var slides = $('.imageslidepane');
        if (slides.length) {
            var url = '@@prettyalbum_json_data';
            $.getJSON(url, function(data) {
                slides.scrollable({
                    circular: false,
                    mousewheel: true,
                    onBeforeSeek: function(event, index) {
                        var api = this;
                        var item = api.getItems().get(index);
                        if (!item) {
                            return false;
                        }
                        var src = data.images[index];
                        $('img', item)
                            .attr('src', data.images[index] + '/image_large')
                            .attr('alt', data.titles[index]);
                        $('.slideimagetitle').html(data.titles[index]);
                        $('.slideimagedescription').html(
                            data.descriptions[index]);
                    }
                }).navigator({
                    navi: '.imageslidetabs',
                    naviItem: 'a',
                    activeClass: 'current',
                    history: false
                });
                var api = slides.data('scrollable');
                $('img', slides).bind('click', function() {
                    api.next();
                });
            });
        }
    });

})(jQuery);