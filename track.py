class Track(object):
    """Tracks have the following attributes:
    
        name:               A string representing the track's name.
        album:              A string representing the track's album.
        artist:             A string representing the track's artist.
        
        sp_uri:             A string representing the track's Spotify URI.
        sp_id:              A string representing the track's Spotify ID.
        sp_album_id:        A string representing the track's album's Spotify ID.
        sp_artist_id:       A string representing the track's artist's Spotify ID.
        
        mb_id:              A string representing the track's Musicbrainz ID.
        mb_album_id:        A string representing the track's Album's Musicbrainz ID.
        mb_artist_id:        A string representing the track's Artist's Musicbrainz ID.
        
        have_track:         A boolean representing whether the track is in Headphones library.
        have_album:         A boolean representing whether the track's album is in Headphones library.
        
        dl_request_status:  A string representing the outcome of adding album to Headphones queue.
    """

    def __init__(self, name, album, artist, uri, sp_uri, sp_id, sp_album_id, sp_artist_id):
        self.name               = name
        self.album              = album
        self.artist             = artist
        
        self.sp_uri             = sp_uri
        self.sp_id              = sp_id
        self.sp_album_id        = sp_album_id
        self.sp_artist_id       = sp_artist_id
        
        self.mb_id              = self.__getMB_id(sp_id)
        self.mb_album_id        = self.__getMB_album_id(mb_artist_id, album)
        self.mb_artist_id       = self.__getMB_artist_id(sp_id)
        
        self.have_track         = False
        self.have_album         = False
        
        self.dl_request_status  = ""
        
    def __getMB_id(self, sp_id):
        # necessary?
    def __getMB_album_id(self, mb_artist_id, album):
        # query Headphones api
    def __getMB_artist_id(self, sp_id):
        ''' Use EchoNest API to map Spotify artist id to Musicbrainz artist id
        '''
        en = pyen.Pyen(ConfigSectionMap("ECHONEST")['api_key'])
        params = {
            'id':       'spotify:artist:' + artistSPID,
            'bucket':   ['id:musicbrainz'],
        }
        response = en.get('artist/profile', **params)
        if (response['status']['message'] == 'Success'):
            mbid = response['artist']['foreign_ids'][0]['foreign_id']
            return mbid[19:]    #remove 'musicbrainz:artist:'
        else:
            return 'notfound'