(function() {

	
	function hasParent( e, p ) {
		if (!e) return false;
		var el = e.target||e.srcElement||e||false;
		while (el && el != p) {
			el = el.parentNode||false;
		}
		return (el!==false);
	};

	var bodyEl = document.body,
		openbtn = document.getElementById( 'open-button' ),
		closebtn = document.getElementById( 'close-button' ),
		closebtnsub = document.getElementById( 'close-button-sub' ),
		caldays = [].slice.call( document.getElementById( 'calendar' ).querySelectorAll( '.fc-body > div.fc-row > div' ) ),
		menu = document.querySelector( '.menu-wrap[data-level="1"]' ),
		submenu = document.querySelector( '.menu-wrap[data-level="2"]' ),
		isMenuOpen = false, isSubMenuOpen = false;

	function init() {
		initEvents();
	}

	function initEvents() {
		openbtn.addEventListener( 'click', toggleMenu );
		
		if( closebtn ) {
			closebtn.addEventListener( 'click', toggleMenu );
		}

		caldays.forEach( function( cell ) {
			if( cell.hasChildNodes() ) {
				cell.addEventListener( 'click', toggleSubMenu );
			}
		} );

		if( closebtnsub ) {
			closebtnsub.addEventListener( 'click', toggleSubMenu );
		}

		document.addEventListener( 'mousedown', function(ev) {
			var target = ev.target;
			
			if( isSubMenuOpen ) {
				if( target !== submenu && target !== closebtnsub && !hasParent( target, submenu ) ) {
					closeMenus();
				}
			}
			else if( isMenuOpen ) {
				if( target !== menu && target !== closebtn && !hasParent( target, menu ) ) {
					closeMenus();
				}
			}
		} );
	}

	function toggleMenu() {
		if( isMenuOpen ) {
			classie.remove( bodyEl, 'show-menu' );
		}
		else {
			classie.add( bodyEl, 'show-menu' );
		}
		isMenuOpen = !isMenuOpen;
	}

	function toggleSubMenu() {
		if( isSubMenuOpen ) {
			classie.remove( bodyEl, 'show-submenu' );
		}
		else {
			classie.add( bodyEl, 'show-submenu' );
		}
		isSubMenuOpen = !isSubMenuOpen;
	}

	function closeMenus() {
		if( isSubMenuOpen ) {
			toggleSubMenu();
		}
		if( isMenuOpen ) {
			toggleMenu();
		}
	}

	init();

})();