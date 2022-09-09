#------------------------------------------------------------------------------
# 
#   https://github.com/jedbot
# 
#   a python class for handling csv data.
# 
#   class needs a file path & a primary field for table
# 
#   data = csv_file ( filePath , keyField ) # example
# 
#------------------------------------------------------------------------------

from csv import reader

class csv_file :

    def __init__ ( self , filePath , keyField ) :

#------------------------------------------------------------------------------
#   class attribute self.records
#------------------------------------------------------------------------------

        self.records = [  ]

        with open ( filePath , newline = '' ) as file :

            csv_table = reader ( file )

            for record in csv_table :

                self.records.append ( record )

            file.close (  )

#------------------------------------------------------------------------------
#   class attribute self.head
#------------------------------------------------------------------------------

        self.head = self.records.pop ( 0 )

#------------------------------------------------------------------------------
#   class attribute self.dataMap
#------------------------------------------------------------------------------
        
        self.dataMap = {  }

        key_index = self.head.index ( keyField )
        
        for record in self.records :

            # get key from index in record
            key = record [ key_index ]

            # add key to dataMap
            self.dataMap [ key ] = {  }

#------------------------------------------------------------------------------
#   finish adding key : val to dataMap
#------------------------------------------------------------------------------

            for field in self.head :

                field_index = self.head.index ( field )

                # add to record { field : cell value }
                self.dataMap [ key ] [ field ] = record [ field_index ]

#------------------------------------------------------------------------------
#   class attribute self.keys
#------------------------------------------------------------------------------

        self.keys = self.dataMap.keys (  )

#------------------------------------------------------------------------------
#   appendix
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#
#   get the value of a cell:
# 
#   dataMap [ 'key' ] [ 'field' ] = cell# 
#
#------------------------------------------------------------------------------

