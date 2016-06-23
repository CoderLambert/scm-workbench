'''
 ====================================================================
 Copyright (c) 2003-2016 Barry A Scott.  All rights reserved.

 This software is licensed as described in the file LICENSE.txt,
 which you should have received as part of this distribution.

 ====================================================================

    wb_svn_ui_components.py.py

'''
import wb_ui_components
import wb_svn_project
import wb_svn_properties_dialog
import wb_svn_info_dialog


class SvnMainWindowComponents(wb_ui_components.WbMainWindowComponents):
    def __init__( self ):
        super().__init__( 'svn' )

    def setupDebug( self ):
        self._debug = self.main_window.app._debugSvnUi

    def setupMenuBar( self, mb, addMenu ):
        # ----------------------------------------
        m = mb.addMenu( T_('&Svn Information') )
        self.all_menus.append( m )

        addMenu( m, T_('Diff Base vs. Working'), self.treeTableActionSvnDiffBaseVsWorking, self.enablerTreeTableSvnDiffBaseVsWorking, 'toolbar_images/diff.png' )
        addMenu( m, T_('Diff HEAD vs. Working'), self.treeTableActionSvnDiffHeadVsWorking, self.enablerTreeTableSvnDiffHeadVsWorking, 'toolbar_images/diff.png' )

        m.addSeparator()
        addMenu( m, T_('Info'), self.treeTableActionSvnInfo, self.enablerTreeTableSvnInfo, 'toolbar_images/info.png' )
        addMenu( m, T_('Properties'), self.treeTableActionSvnProperties, self.enablerTreeTableSvnProperties, 'toolbar_images/property.png' )
        m.addSeparator()
        addMenu( m, T_('Log History'), self.treeTableActionSvnLogHistory, self.enablerTreeTableSvnLogHistory, 'toolbar_images/history.png' )
        addMenu( m, T_('Status'), self.treeActionSvnStatus )

        # ----------------------------------------
        m = mb.addMenu( T_('&Git Actions') )
        self.all_menus.append( m )

        addMenu( m, T_('Add'), self.tableActionSvnAdd, self.enablerSvnAdd, 'toolbar_images/add.png' )
        addMenu( m, T_('Revert'), self.tableActionSvnRevert, self.enablerSvnRevert, 'toolbar_images/revert.png' )

        m.addSeparator()
        addMenu( m, T_('Delete…'), self.tableActionSvnDelete, self.main_window.enablerFilesExists )

        m.addSeparator()
        addMenu( m, T_('Checkin…'), self.treeActionSvnCheckin, self.enablerSvnCheckin, 'toolbar_images/checkin.png' )

        m.addSeparator()
        addMenu( m, T_('Update…'), self.treeActionSvnUpdate, icon_name='toolbar_images/update.png' )

    def setupToolBarAtLeft( self, addToolBar, addTool ):
        t = addToolBar( T_('svn logo'), style='font-size: 20pt; width: 32px; color: #000099' )
        self.all_toolbars.append( t )

        addTool( t, 'Svn', self.main_window.projectActionSettings )

    def setupToolBarAtRight( self, addToolBar, addTool ):
        # ----------------------------------------
        t = addToolBar( T_('svn info') )
        self.all_toolbars.append( t )

        addTool( t, T_('Diff'), self.treeTableActionSvnDiffBaseVsWorking, self.enablerTreeTableSvnDiffBaseVsWorking, 'toolbar_images/diff.png' )
        addTool( t, T_('Log History'), self.treeTableActionSvnLogHistory, self.enablerTreeTableSvnLogHistory, 'toolbar_images/history.png' )
        addTool( t, T_('Info'), self.treeTableActionSvnInfo, self.enablerTreeTableSvnInfo, 'toolbar_images/info.png' )
        addTool( t, T_('Properties'), self.treeTableActionSvnProperties, self.enablerTreeTableSvnProperties, 'toolbar_images/property.png' )

        # ----------------------------------------
        t = addToolBar( T_('svn state') )
        self.all_toolbars.append( t )

        addTool( t, T_('Add'), self.tableActionSvnAdd, self.enablerSvnAdd, 'toolbar_images/add.png' )
        addTool( t, T_('Revert'), self.tableActionSvnRevert, self.enablerSvnRevert, 'toolbar_images/revert.png' )
        t.addSeparator()
        addTool( t, T_('Checkin'), self.treeActionSvnCheckin, self.enablerSvnCheckin, 'toolbar_images/checkin.png' )
        t.addSeparator()
        addTool( t, T_('Update'), self.treeActionSvnUpdate, icon_name='toolbar_images/update.png' )

    def setupTableContextMenu( self, m, addMenu ):
        super().setupTableContextMenu( m, addMenu )

        m.addSection( T_('Diff') )
        addMenu( m, T_('Diff Base vs. Working'), self.tableActionSvnDiffBaseVsWorking, self.enablerTableSvnDiffBaseVsWorking, 'toolbar_images/diff.png' )
        addMenu( m, T_('Diff HEAD vs. Working'), self.tableActionSvnDiffHeadVsWorking, self.enablerTableSvnDiffHeadVsWorking, 'toolbar_images/diff.png' )

        m.addSection( T_('Info' ) )
        addMenu( m, T_('Information'), self.treeTableActionSvnInfo, self.enablerTreeTableSvnInfo, 'toolbar_images/info.png' )
        addMenu( m, T_('Properties'), self.treeTableActionSvnProperties, self.enablerTreeTableSvnProperties, 'toolbar_images/property.png' )

        m.addSection( T_('Status') )
        addMenu( m, T_('Log History'), self.treeTableActionSvnLogHistory, self.enablerTreeTableSvnLogHistory, 'toolbar_images/history.png' )

    def setupTreeContextMenu( self, m, addMenu ):
        super().setupTreeContextMenu( m, addMenu )

        m.addSection( T_('Diff') )
        addMenu( m, T_('Diff Base vs. Working'), self.treeActionSvnDiffBaseVsWorking, self.enablerTreeSvnDiffBaseVsWorking, 'toolbar_images/diff.png' )
        addMenu( m, T_('Diff HEAD vs. Working'), self.treeActionSvnDiffHeadVsWorking, self.enablerTreeSvnDiffHeadVsWorking, 'toolbar_images/diff.png' )

        m.addSection( T_('Info' ) )
        addMenu( m, T_('Information'), self.treeTableActionSvnInfo, self.enablerTreeTableSvnInfo, 'toolbar_images/info.png' )
        addMenu( m, T_('Properties'), self.treeTableActionSvnProperties, self.enablerTreeTableSvnProperties, 'toolbar_images/property.png' )

        m.addSection( T_('Status') )
        addMenu( m, T_('Log History'), self.treeTableActionSvnLogHistory, self.enablerTreeTableSvnLogHistory, 'toolbar_images/history.png' )

    #--- Enablers ---------------------------------------------------------

    #------------------------------------------------------------
    #
    # tree or table actions depending on focus
    #
    #------------------------------------------------------------
    def enablerTreeTableSvnInfo( self ):
        return self.main_window.callTreeOrTableFunction( self.enablerTreeSvnInfo, self.enablerTableSvnInfo, default=False )

    def enablerTreeTableSvnProperties( self ):
        return self.main_window.callTreeOrTableFunction( self.enablerTreeSvnProperties, self.enablerTableSvnProperties, default=False )

    def enablerTreeTableSvnDiffBaseVsWorking( self ):
        return self.main_window.callTreeOrTableFunction( self.enablerTreeSvnDiffBaseVsWorking, self.enablerTableSvnDiffBaseVsWorking, default=False )

    def enablerTreeTableSvnDiffHeadVsWorking( self ):
        return self.main_window.callTreeOrTableFunction( self.enablerTreeSvnDiffHeadVsWorking, self.enablerTableSvnDiffHeadVsWorking, default=False )

    def enablerTreeTableSvnLogHistory( self ):
        return self.main_window.callTreeOrTableFunction( self.enablerTreeSvnLogHistory, self.enablerTableSvnLogHistory, default=False )

    # ------------------------------------------------------------
    def treeTableActionSvnDiffBaseVsWorking( self ):
        self.main_window.callTreeOrTableFunction( self.treeActionSvnDiffBaseVsWorking, self.tableActionSvnDiffBaseVsWorking )

    def treeTableActionSvnDiffHeadVsWorking( self ):
        self.main_window.callTreeOrTableFunction( self.treeActionSvnDiffHeadVsWorking, self.tableActionSvnDiffHeadVsWorking )

    def treeTableActionSvnLogHistory( self ):
        self.main_window.callTreeOrTableFunction( self.treeActionSvnLogHistory, self.tableActionSvnLogHistory )

    def treeTableActionSvnInfo( self ):
        self.main_window.callTreeOrTableFunction( self.treeActionSvnInfo, self.tableActionSvnInfo )

    def treeTableActionSvnProperties( self ):
        self.main_window.callTreeOrTableFunction( self.treeActionSvnProperties, self.tableActionSvnProperties )

    #------------------------------------------------------------
    #
    # tree actions
    #
    #------------------------------------------------------------
    def enablerTreeSvnDiffBaseVsWorking( self ):
        return self.__enablerTreeSvnIsControlled()

    def enablerTreeSvnDiffHeadVsWorking( self ):
        return self.__enablerTreeSvnIsControlled()

    def enablerTreeSvnLogHistory( self ):
        return self.__enablerTreeSvnIsControlled()

    def enablerTreeSvnInfo( self ):
        return self.__enablerTreeSvnIsControlled()

    def enablerTreeSvnProperties( self ):
        return self.__enablerTreeSvnIsControlled()

    def __enablerTreeSvnIsControlled( self ):
        tree_node = self.selectedSvnProjectTreeNode()
        if tree_node is None:
            return False

        tree_node.relativePath()

        if not tree_node.project.hasFileState( tree_node.relativePath() ):
            return False

        file_state = tree_node.project.getFileState( tree_node.relativePath() )
        return file_state.isControlled()

    # ------------------------------------------------------------
    def treeActionSvnDiffBaseVsWorking( self ):
        tree_node = self.selectedSvnProjectTreeNode()
        if tree_node is None:
            return

        diff_text = tree_node.project.cmdDiffFolder( tree_node.relativePath(), head=False )
        self.main_window.showDiffText( 'Diff Base vs. Working from %s' % (tree_node.relativePath(),), diff_text.split('\n') )

    def treeActionSvnDiffHeadVsWorking( self ):
        tree_node = self.selectedSvnProjectTreeNode()
        if tree_node is None:
            return

        diff_text = tree_node.project.cmdDiffFolder( tree_node.relativePath(), head=True )
        self.main_window.showDiffText( 'Diff Head vs. Working from %s' % (tree_node.relativePath(),), diff_text )

    def treeActionSvnInfo( self ):
        tree_node = self.selectedSvnProjectTreeNode()
        if tree_node is None:
            return

        project = tree_node.project
        info = project.cmdInfo( tree_node.relativePath() )

        dialog = wb_svn_info_dialog.InfoDialog( self.app, self.main_window, tree_node.relativePath(), tree_node.absolutePath(), info )
        dialog.exec_()

    def treeActionSvnProperties( self ):
        tree_node = self.selectedSvnProjectTreeNode()
        if tree_node is None:
            return

        project = tree_node.project
        filename = tree_node.relativePath()
        prop_dict = project.cmdPropList( filename )

        dialog = wb_svn_properties_dialog.FolderPropertiesDialog( self.app, self.main_window, filename, prop_dict )
        if dialog.exec_():
            for is_present, name, value in dialog.getModifiedProperties():
                if not is_present:
                    # delete name
                    project.cmdPropDel( name, filename )

                else:
                    # add/update name value
                    project.cmdPropSet( name, value, filename )

        self.main_window.updateTableView()

    def treeActionSvnLogHistory( self ):
        print( 'treeActionSvnLogHistory' )

    def treeActionSvnCheckin( self ):
        pass

    def treeActionSvnUpdate( self ):
        pass

    def treeActionSvnStatus( self ):
        pass

    #------------------------------------------------------------
    #
    # table actions
    #
    #------------------------------------------------------------
    def enablerTableSvnDiffBaseVsWorking( self ):
        if not self.isScmTypeActive():
            return False

        all_file_state = self.tableSelectedAllFileStates()
        if len(all_file_state) == 0:
            return False

        for file_state in all_file_state:
            if not file_state.isModified():
                return False

        return True

    def enablerTableSvnDiffHeadVsWorking( self ):
        if not self.isScmTypeActive():
            return False

        return True

    def enablerTableSvnLogHistory( self ):
        if not self.isScmTypeActive():
            return False

        return True

    def enablerTableSvnInfo( self ):
        return self.__enablerSvnFilesControlled()

    def enablerTableSvnProperties( self ):
        return self.__enablerSvnFilesControlled()

    def enablerSvnAdd( self ):
        # can only add uncontrolled files
        return self.__enablerSvnFilesUncontrolled()

    def enablerSvnRevert( self ):
        # can only revert uncontrolled files
        return self.__enablerSvnFilesControlled()

    def __enablerSvnFilesUncontrolled( self ):
        all_file_state = self.tableSelectedAllFileStates()
        if len(all_file_state) == 0:
            return False

        for file_state in all_file_state:
            if not file_state.isUncontrolled():
                return False

        return True

    def __enablerSvnFilesControlled( self ):
        all_file_state = self.tableSelectedAllFileStates()
        if len(all_file_state) == 0:
            return False

        for file_state in all_file_state:
            if not file_state.isControlled():
                return False

        return True

    def enablerSvnCheckin( self ):
        all_file_states = self.tableSelectedAllFileStates()
        if len( all_file_states ) == 0:
            # check in what ever in in the tree
            tree_node = self.selectedSvnProjectTreeNode()
            if tree_node is None:
                return False

            return tree_node.project.numUncommittedFiles() > 0

        # check in only the selected files
        return self.__enablerSvnFilesControlled()

    def __enablerSvnFilesModified( self ):
        all_file_state = self.tableSelectedAllFileStates()
        if len(all_file_state) == 0:
            return False

        for file_state in all_file_state:
            if not (file_state.isAdded() or file_state.isModified() or file_state.isDeleted()):
                return False

        return True

    # ------------------------------------------------------------
    def tableActionSvnDiffBaseVsWorking( self ):
        for file_state in self.tableSelectedAllFileStates():
            self.main_window.diffTwoFiles(
                    file_state.getTextLinesBase(),
                    file_state.getTextLinesWorking(),
                    T_('Diff Base vs. Working %s') % (file_state.filePath(),),
                    T_('Base %s') % (file_state.filePath(),),
                    T_('Working %s') % (file_state.filePath(),)
                    )

    def tableActionSvnDiffHeadVsWorking( self ):
        for file_state in self.tableSelectedAllFileStates():
            self.main_window.diffTwoFiles(
                    file_state.getTextLinesBase(),
                    file_state.getTextLinesWorking(),
                    T_('Diff HEAD vs. Working %s') % (file_state.filePath(),),
                    T_('HEAD %s') % (file_state.filePath(),),
                    T_('Working %s') % (file_state.filePath(),)
                    )

    def tableActionSvnInfo( self ):
        def action( project, filename ):
            info = project.cmdInfo( filename )

            dialog = wb_svn_info_dialog.InfoDialog( self.app, self.main_window, filename, project.pathForSvn( filename ), info )
            dialog.exec_()

        self.__tableActionSvnCmd( action )

    def tableActionSvnProperties( self ):
        def action( project, filename ):
            prop_dict = project.cmdPropList( filename )

            dialog = wb_svn_properties_dialog.FilePropertiesDialog( self.app, self.main_window, filename, prop_dict )
            if dialog.exec_():
                for is_present, name, value in dialog.getModifiedProperties():
                    if not is_present:
                        # delete name
                        project.cmdPropDel( name, filename )
                    else:
                        # add/update name value
                        project.cmdPropSet( name, value, filename )

            self.main_window.updateTableView()

        self.__tableActionSvnCmd( action )

    def tableActionSvnLogHistory( self ):
        print( 'tableActionSvnLogHistory' )

    def tableActionSvnAdd( self ):
        def action( project, filename ):
            project.cmdAdd( filename )

        self.__tableActionSvnCmd( action )

    def tableActionSvnRevert( self ):
        def action( project, filename ):
            project.cmdRevert( filename )

        self.__tableActionSvnCmd( action )

    def tableActionSvnDelete( self ):
        def action( project, filename ):
            project.cmdDelete( filename )

        self.__tableActionSvnCmd( action )

    def __tableActionSvnCmd( self, cmd ):
        tree_node = self.selectedSvnProjectTreeNode()
        if tree_node is None:
            return

        project = tree_node.project

        try:
            for file_state in self.tableSelectedAllFileStates():
                cmd( project, file_state.filePath() )

        except wb_svn_project.ClientError as e:
            all_client_error_lines = project.clientErrorToStrList( e )
            for line in all_client_error_lines:
                self.app.log.error( line )

            self.main_window.errorMessage( 'Svn Error', '\n'.join( all_client_error_lines ) )

        self.main_window.updateTableView()


    # ------------------------------------------------------------
    def selectedSvnProjectTreeNode( self ):
        if not self.isScmTypeActive():
            return None

        tree_node = self.main_window.selectedScmProjectTreeNode()
        assert isinstance( tree_node, wb_svn_project.SvnProjectTreeNode )
        return tree_node
