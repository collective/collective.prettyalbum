import json
import random
from Products.Five import BrowserView


class AlbumsView(BrowserView):
    
    @property
    def scale(self):
        return 'thumb'
    
    @property
    def albums(self):
        ret = list()
        result = self.context.atctListAlbum(
            images=0, folders=1, subimages=0, others=0)
        albums = list()
        for brain in result['folders']:
            obj = brain.getObject()
            direct = obj.getLayout() == 'slide_view'
            images = self.context.portal_catalog({
                'portal_type': 'Image',
                'sort_on': 'getObjPositionInParent',
                'path': {
                    'query': brain.getPath(),
                    'depth': 1,
                },
            })
            album = dict()
            album['title'] = brain.Title
            album['description'] = brain.Description.replace('\r\n', '<br />')
            album['direct'] = direct
            album['url'] = obj.absolute_url()
            album['preview'] = None
            album['preview_style'] = None
            album['urls'] = list()
            album['titles'] = list()
            album['descriptions'] = list()
            if bool(images):
                image = random.choice(images).getObject()
                height = image.getHeight(scale=self.scale)
                padding = (140 - image.getHeight(scale=self.scale)) / 2
                style = 'padding-bottom:%ipx;padding-top:%ipx;' \
                    % (padding, padding)
                album['preview'] = image
                album['preview_style'] = style
            for image_brain in images:
                album['urls'].append(image_brain.getURL())
                album['titles'].append(image_brain.Title)
                album['descriptions'].append(image_brain.Description)
            albums.append(album)
        for album in albums:
            album['urls'] = json.dumps(album['urls'])
            album['titles'] = json.dumps(album['titles'])
            album['descriptions'] = json.dumps(album['descriptions'])
        return albums


class ImageData(BrowserView):
    
    @property
    def image_data(self):
        ret = {
            'images': list(),
            'titles': list(),
            'descriptions': list(),
            #'info': list(),
        }
        images = self.context.portal_catalog({
            'portal_type': 'Image',
            'sort_on': 'getObjPositionInParent',
            'path': {
                'query': '/'.join(self.context.getPhysicalPath()),
                'depth': 1,
            },
        })
        for brain in images:
            #img = brain.getObject()
            ret['images'].append(brain.getURL())
            ret['titles'].append(brain.Title)
            ret['descriptions'].append(brain.Description)
            #ret['info'].append({
            #    'width': img.getWidth('large'),
            #    'height': img.getHeight('large'),
            #})
        return ret


class JSONView(ImageData):
    
    def prettyalbum_json_data(self):
        return json.dumps(self.image_data)


class SlideView(ImageData):
    
    @property
    def count(self):
        return len(self.image_data['images'])