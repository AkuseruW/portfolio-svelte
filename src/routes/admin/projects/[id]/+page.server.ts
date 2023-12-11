import type { PageServerLoad, Actions } from './$types';
import { SERVEUR_URL } from '$env/static/private'
import { error } from '@sveltejs/kit';


export const load: PageServerLoad = async ({ params }) => {
    const project = await fetch(`${SERVEUR_URL}/api/projects/${params.id}`).then(res => res.json())
    const skills = await fetch(`${SERVEUR_URL}/api/skills/`).then(res => res.json())
    
    if (project) {
        return {
            project,
            skills
        }
    }

    throw error(404, 'Project not found');
}


export const actions: Actions = {
    update_category: async ({ request }) => {
        const formData = await request.formData();
        const name = formData.get('name');

        if (!name) {
            return {
                error: 'Name is required'
            }
        }

        const category = {
            name
        }

        const res = await fetch(`${SERVEUR_URL}/api/categories/${formData.get('id')}`, {
            method: 'PATCH',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(category),
        })

        if (res.ok) {
            return { success: true };
        } else {
            return {
                error: 'Failed to update category'
            }
        }
    }

}