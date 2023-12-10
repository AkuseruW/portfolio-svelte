import type { PageServerLoad, Actions } from './$types';
import { SERVEUR_URL } from '$env/static/private'
import { writeFile } from 'fs/promises';


export const load: PageServerLoad = () => {
    const categories = async () => {
        return await fetch(`${SERVEUR_URL}/api/categories/`).then(res => res.json())
    }

    return {
        categories: categories()
    }
}


export const actions: Actions = {
    create_skill: async ({ request }) => {
        const formData = await request.formData();
        
        await fetch(`${SERVEUR_URL}/api/skills/`, {
            method: 'POST',
            body: formData
        })

        return { success: true };
    }

}